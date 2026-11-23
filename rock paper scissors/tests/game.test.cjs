const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');

const html = fs.readFileSync(path.join(__dirname, '..', 'index.html'), 'utf8');
const script = html.match(/<script>([\s\S]*?)<\/script>/)[1];
const reset = html.match(/<button onclick="([^"]*)">Reset Score<\/button>/)[1];
const moves = ['rock', 'paper', 'scissors'];

function game(random, storage = new Map()) {
  const messages = [];
  const context = vm.createContext({
    Math: { random: () => random },
    localStorage: {
      getItem: key => storage.get(key) ?? null,
      setItem: (key, value) => storage.set(key, value),
      removeItem: key => storage.delete(key),
    },
    alert: message => messages.push(message),
  });
  vm.runInContext(script, context);
  return { context, storage, messages };
}

for (const [playerIndex, player] of moves.entries()) {
  for (const [computerIndex, computer] of moves.entries()) {
    test(`${player} versus ${computer}`, () => {
      const { context, storage, messages } = game((computerIndex + 0.5) / 3);
      vm.runInContext(`playGame('${player}')`, context);
      const difference = (playerIndex - computerIndex + 3) % 3;
      const expected = difference === 0 ? 'ties' : difference === 1 ? 'wins' : 'losses';
      const score = JSON.parse(storage.get('score'));
      assert.equal(score[expected], 1);
      assert.equal(score.wins + score.losses + score.ties, 1);
      assert.ok(messages[0].includes(`computer picked: ${computer}`));
    });
  }
}

test('score persists across a new page context and reset clears storage/counters', () => {
  const first = game(0.1);
  vm.runInContext("playGame('paper')", first.context);
  const second = game(0.1, first.storage);
  vm.runInContext("playGame('paper')", second.context);
  assert.equal(JSON.parse(second.storage.get('score')).wins, 2);
  vm.runInContext(reset, second.context);
  assert.equal(second.storage.has('score'), false);
  vm.runInContext("playGame('rock')", second.context);
  assert.deepEqual(JSON.parse(second.storage.get('score')), { wins: 0, losses: 0, ties: 1 });
});
