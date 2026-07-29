$("input:button").click(function () {
  var seatCode = $("#seatCode").val();
  var seatNumber = parseInt($("#seatNumber").val());
  var noOfTickets = parseInt($("#noOfTickets").val());

  var res = $("#result");
  console.log(noOfTickets);

  if (seatNumber + noOfTickets - 1 <= 4) {
    var c = seatNumber;
    $("table tbody tr td").each(function (index, val) {
      if ($(val).text().substr(0, 1) === seatCode) {
        if (c <= noOfTickets) {
          $(val).css("background-color", "green");
          c++;
        } else {
          return false;
        }
        console.log(val, c);
      }
    });
    res.text("You can pay Rs." + noOfTickets * 650);
  } else {
    var count = 5 - seatNumber;
    for (var i = seatNumber; i < 5; i++) {
      var selector = "#" + seatCode + i;
      $(selector).css("background-color", "red");
    }
    res.text(
      "Sorry !!! There is/are only " +
        count +
        " ticket(s) available in " +
        seatCode +
        ". starting from seat Number " +
        seatNumber
    );
  }
});
