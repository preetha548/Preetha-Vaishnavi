/*
 * IS NOT FINISHED
 */

/* Small Graphic Engine -> 3D */
var gEngine = {
  /* Initialization */
  __vars_ratio: null,
  init: function(selector) {
    var cvs = document.querySelector(selector);
    cvs._ctx = cvs.getContext("2d");
    /* Quality */
    cvs._autoSize = function(factor) {
      factor = factor || 1;
      this.__vars_ratio = cvs.offsetHeight / cvs.offsetWidth;
      cvs.width = cvs.parentNode.offsetWidth * factor;
      cvs.height = cvs.width * this.__vars_ratio * factor;
    };
    cvs._autoSize();
    return cvs;
  },
  /* Model: Cube */
  __vars_u: 0.5,
  cube: function() {
    return {
      center: [0, 0, 0],
      points: [
        [-this.__vars_u, -this.__vars_u, -this.__vars_u],
        [this.__vars_u, -this.__vars_u, -this.__vars_u],
        [this.__vars_u, this.__vars_u, -this.__vars_u],
        [-this.__vars_u, this.__vars_u, -this.__vars_u],
        [-this.__vars_u, -this.__vars_u, this.__vars_u],
        [this.__vars_u, -this.__vars_u, this.__vars_u],
        [this.__vars_u, this.__vars_u, this.__vars_u],
        [-this.__vars_u, this.__vars_u, this.__vars_u]
      ],
      edges: [
        [0, 1],
        [1, 2],
        [2, 3],
        [3, 0],
        [4, 5],
        [5, 6],
        [6, 7],
        [7, 4],
        [0, 4],
        [1, 5],
        [2, 6],
        [3, 7]
      ],
      faces: [
        [0, 1, 2, 3],
        [4, 5, 6, 7],
        [0, 1, 5, 4],
        [2, 3, 7, 6],
        [1, 2, 6, 5],
        [3, 0, 4, 7]
      ]
    };
  },
  /* Drawing */
  __vars_points: [],
  draw: function(cvs, camera, screen, shapes, wireMode) {
    var self = this;
    cvs._ctx.clearRect(0, 0, cvs.width, cvs.height);
    /* For each shape */
    shapes.map(function(shape) {
      /* For each point */
      this.__vars_points = shape.points
        .map(function(point) {
          /* Projection */
          return self.pt3D(point, camera, screen);
        })
        .filter(function(point) {
          /* Remove the hide points */
          return point[2] >= 0;
        });
      /* Wire mode or Render RT */
      if (wireMode || false) {
        /* For each edge */
        shape.edges.map(function(edge) {
          /* Remove the hide edge */
          edge = edge
            .map(function(index) {
              return this.__vars_points[index] || null;
            })
            .filter(function(item) {
              return item !== null;
            });
          /* Draw the edge */
          if (edge.length === 2) {
            self.drawPolygon(cvs._ctx, {
              data: edge,
              color: "rgba(0,0,0,0)",
              borderColor: "rgba(0,0,50,.2)",
              border: 1,
              mode: 0
            });
          }
          return edge;
        });
      } else {
        /* For each face */
        shape.faces.map(function(face) {
          /* Remove the hide faces */
          face = face
            .map(function(index) {
              return this.__vars_points[index] || null;
            })
            .filter(function(item) {
              return item !== null;
            });
          /* Draw the face */
          if (face.length > 2) {
            self.drawPolygon(cvs._ctx, {
              data: face,
              color: "rgba(0,100,150,.4)",
              borderColor: "rgba(0,0,0,.1)",
              border: 1,
              mode: 1
            });
          }
          return shape;
        });
      }
      return shape;
    });
  },
  /* Draw a polygon */
  __vars_iDP: 0,
  drawPolygon: function(ctx, args) {
    ctx.beginPath();
    ctx.fillStyle = args.color || "#000";
    ctx.lineWidth = args.border || 1;
    ctx.strokeStyle = args.borderColor || "rgba(0,0,0,.1)";
    ctx.moveTo(args.data[0][0], args.data[0][1]);
    for (
      this.__vars_iDP = 1;
      this.__vars_iDP < args.data.length;
      this.__vars_iDP++
    ) {
      ctx.lineTo(args.data[this.__vars_iDP][0], args.data[this.__vars_iDP][1]);
    }
    ctx.lineTo(args.data[0][0], args.data[0][1]);
    if (args.mode || 0) {
      ctx.fill();
    } else {
      ctx.stroke();
    }
    ctx.stroke();
    ctx.closePath();
  },
  /* Optimization */
  __vars_view: null,
  __vars_pt: [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
  __vars_flat_pt: [0, 0, 0],
  __vars_cache_rot: [0, 0, 0, null],
  /* Projection - 3D -> 2D */
  pt3D: function(point, camera, screen) {
    /* Optimization - clean up */
    this.__vars_pt[0][1] = 0;
    this.__vars_pt[0][2] = 0;
    this.__vars_pt[1][0] = 0;
    this.__vars_pt[1][2] = 0;
    this.__vars_pt[2][0] = 0;
    this.__vars_pt[2][1] = 0;
    /* Precalculate */
    if (
      this.__vars_cache_rot[0] !== camera[1][0] ||
      this.__vars_cache_rot[1] !== camera[1][1] ||
      this.__vars_cache_rot[2] !== camera[1][2] ||
      this.__vars_cache_rot[3] === null
    ) {
      this.__vars_cache_rot[0] = camera[1][0];
      this.__vars_cache_rot[1] = camera[1][1];
      this.__vars_cache_rot[2] = camera[1][2];
      this.__vars_cache_rot[3] = this.mtxRotXYZ(
        -this.toRadian(camera[1][0]),
        -this.toRadian(camera[1][1]),
        -this.toRadian(camera[1][2])
      );
    }
    /* Translation */
    this.__vars_pt[0][0] = point[0] - camera[0][0];
    this.__vars_pt[1][1] = point[1] - camera[0][1];
    this.__vars_pt[2][2] = point[2] - camera[0][2];
    /* Rotate */
    this.__vars_pt = this.mtxProduct3x3(
      this.__vars_pt,
      this.__vars_cache_rot[3]
    );
    this.__vars_flat_pt[0] =
      this.__vars_pt[0][0] + this.__vars_pt[1][0] + this.__vars_pt[2][0];
    this.__vars_flat_pt[1] =
      this.__vars_pt[0][1] + this.__vars_pt[1][1] + this.__vars_pt[2][1];
    this.__vars_flat_pt[2] =
      this.__vars_pt[0][2] + this.__vars_pt[1][2] + this.__vars_pt[2][2];
    /* Projection */
    this.__vars_view = screen[2] / (this.__vars_flat_pt[2] + screen[3] || 1);
    return [
      this.__vars_flat_pt[0] * this.__vars_view + screen[0] / 2,
      this.__vars_flat_pt[1] * -this.__vars_view + screen[1] / 2,
      Math.sqrt(
        this.__vars_flat_pt[0] * this.__vars_flat_pt[0] +
          this.__vars_flat_pt[1] * this.__vars_flat_pt[1] +
          this.__vars_flat_pt[2] * this.__vars_flat_pt[2]
      ) * (this.__vars_flat_pt[2] >= 0 ? 1 : -1)
    ];
  },
  /* Scaling */
  __vars_tmpS: [0, 0, 0],
  scaling: function(shape, size) {
    this.__vars_tmpS[0] = shape.center[0];
    this.__vars_tmpS[1] = shape.center[1];
    this.__vars_tmpS[2] = shape.center[2];
    shape.points = shape.points.map(function(pt) {
      return [
        (pt[0] - this.__vars_tmpS[0]) * size + this.__vars_tmpS[0],
        (pt[1] - this.__vars_tmpS[1]) * size + this.__vars_tmpS[1],
        (pt[2] - this.__vars_tmpS[2]) * size + this.__vars_tmpS[2]
      ];
    });
    return shape;
  },
  /* Translate */
  translate: function(shape, x, y, z) {
    shape.center = [
      shape.center[0] + x,
      shape.center[1] + y,
      shape.center[2] + z
    ];
    shape.points = shape.points.map(function(pt) {
      return [pt[0] + x, pt[1] + y, pt[2] + z];
    });
    return shape;
  },
  /* Rotate Matrix - constants */
  rotX: function(t) {
    return [
      [1, 0, 0],
      [0, Math.cos(t), -Math.sin(t)],
      [0, Math.sin(t), Math.cos(t)]
    ];
  },
  rotY: function(t) {
    return [
      [Math.cos(t), 0, Math.sin(t)],
      [0, 1, 0],
      [-Math.sin(t), 0, Math.cos(t)]
    ];
  },
  rotZ: function(t) {
    return [
      [Math.cos(t), -Math.sin(t), 0],
      [Math.sin(t), Math.cos(t), 0],
      [0, 0, 1]
    ];
  },
  /* Matrix product */
  __vars_iMP: 0,
  __vars_jMP: 0,
  __vars_ijMP: 0,
  __vars_kMP: 0,
  __vars_oMP: [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
  mtxProduct3x3: function(a, b) {
    this.__vars_oMP = [[0, 0, 0], [0, 0, 0], [0, 0, 0]];
    for (this.__vars_iMP = 0; this.__vars_iMP < 3; this.__vars_iMP++) {
      for (this.__vars_jMP = 0; this.__vars_jMP < 3; this.__vars_jMP++) {
        this.__vars_ijMP = 0;
        for (this.__vars_kMP = 0; this.__vars_kMP < 3; this.__vars_kMP++) {
          this.__vars_ijMP +=
            a[this.__vars_iMP][this.__vars_kMP] *
            b[this.__vars_kMP][this.__vars_jMP];
        }
        this.__vars_oMP[this.__vars_iMP][this.__vars_jMP] = this.__vars_ijMP;
      }
    }
    return this.__vars_oMP;
  },
  /* Rotation X, Y and Z */
  mtxRotXYZ: function(x, y, z) {
    return this.mtxProduct3x3(
      this.rotZ(z),
      this.mtxProduct3x3(this.rotX(x), this.rotY(y))
    );
  },
  /* Angle to radian */
  toRadian: function(angle) {
    return (angle - 180) * (Math.PI / 180);
  },
  /* Radian to angle */
  toAngle: function(rad) {
    return (rad / (Math.PI / 180) + 180) % 360;
  }
};

/* Small Physic Engine (or something like this :p) */
var pEngine = {
  /* Initialize a map */
  init: function(x, y, dx, dy, dz, spacing) {
    return new Array(x * y).fill(0).map(function(cell, index) {
      /* New cube */
      var cube = gEngine.cube();
      cube.x = index % x;
      cube.y = Math.floor(index / x);
      cube.z = 0;
      /* Translate */
      return gEngine.translate(
        cube,
        spacing * (Math.floor(index / y) + dx),
        spacing * dy,
        spacing * ((index % y) + dz)
      );
    });
  },
  /* Turn and move the camera with the mouse */
  run: function(cvs, camera, screen, map, wireMode) {
    cvs._useMouse = cvs._useMouse || false;
    /* Switch on/off */
    cvs.addEventListener("click", function() {
      cvs._useMouse = !cvs._useMouse;
      cvs.style.cursor = cvs._useMouse ? "none" : "default";
      /* Fullscreen */
      if (cvs._useMouse) {
        cvs.parentNode.className = "app-fullscreen";
        if (cvs.parentNode.requestFullscreen) {
          cvs.parentNode.requestFullscreen();
        }
        if (cvs.parentNode.msRequestFullscreen) {
          cvs.parentNode.msRequestFullscreen();
        }
        if (cvs.parentNode.mozRequestFullScreen) {
          cvs.parentNode.mozRequestFullScreen();
        }
        if (cvs.parentNode.webkitRequestFullScreen) {
          cvs.parentNode.webkitRequestFullScreen();
        }
      } else {
        cvs.parentNode.className = "app";
        if (document.exitFullscreen) {
          document.exitFullscreen();
        }
        if (document.msExitFullscreen) {
          document.msExitFullscreen();
        }
        if (document.mozCancelFullScreen) {
          document.mozCancelFullScreen();
        }
        if (document.webkitExitFullscreen) {
          document.webkitExitFullscreen();
        }
      }
      cvs._autoSize();
      screen = [
        cvs.width,
        cvs.height,
        Math.max(cvs.width, cvs.height) / 2,
        screen[3]
      ];
      gEngine.draw(cvs, camera, screen, map, wireMode || false);
    });
    /* Apply a rotation to the camera */
    var mouse = { x: 0, y: 0, z: 0 };
    /*var diag = Math.sqrt(
      cvs.offsetWidth * cvs.offsetWidth + cvs.offsetHeight * cvs.offsetHeight
    );*/
    //var roll, pitch;
    /*
     * [IN (HARD) WORKING]
     */
    cvs.addEventListener("mousemove", function(e) {
      if (cvs._useMouse) {
        /* Position */
        mouse = { x: e.offsetX, y: e.offsetY };
        mouse.z = Math.sqrt(mouse.x * mouse.x + mouse.y * mouse.y);
        /* Edit the angles */
        camera[1][0] = ((180 / cvs.offsetHeight) * (mouse.y - 270)) % 180;
        camera[1][1] = (((360 / cvs.offsetWidth) * (mouse.x + 360)) % 360) * -1;
        //camera[1][2] = (((360 / diag) * mouse.z + 90) % 360) * -1;
        /* Draw */
        gEngine.draw(cvs, camera, screen, map, wireMode || false);
        /* Mouse dot */
        gEngine.drawPolygon(cvs._ctx, {
          data: [
            [mouse.x - 5, mouse.y - 5],
            [mouse.x + 5, mouse.y - 5],
            [mouse.x + 5, mouse.y + 5],
            [mouse.x - 5, mouse.y + 5]
          ],
          color: "rgba(0,0,0,0.8)",
          borderColor: "rgba(0,0,0,0.3)",
          border: 1,
          mode: 1
        });
      }
    });
    /* Move the camera */
    var vector = 0.4,
      keys = [];
    document.addEventListener("keydown", function(e) {
      if (cvs._useMouse) {
        keys.push(e.keyCode ? e.keyCode : e.which);
      }
    });
    window.setInterval(function() {
      if (keys.length) {
        /* Apply */
        keys = keys
          .map(function(key) {
            key = String.fromCharCode(key).toLowerCase();
            if (key === "z") {
              camera[0][2] += vector;
            }
            if (key === "s") {
              camera[0][2] -= vector;
            }
            if (key === "q") {
              camera[0][0] -= vector;
            }
            if (key === "d") {
              camera[0][0] += vector;
            }
            if (key === "t") {
              camera[0][1] += vector;
            }
            if (key === "g") {
              camera[0][1] -= vector;
            }
            return 0;
          })
          .filter(function() {
            return 0;
          });
        /* Draw */
        gEngine.draw(cvs, camera, screen, map, wireMode || false);
      }
    }, 10);
    /* Draw */
    gEngine.draw(cvs, camera, screen, map, wireMode || false);
  }
};

(function() {
  /* Canvas */
  var cvs = gEngine.init("canvas");

  /* Define the scene */
  var camera = [[0, 0, 0], [0, 0, 0]],
    screen = [cvs.width, cvs.height, Math.max(cvs.width, cvs.height) / 2, 1];

  /* Create a map */
  var map = pEngine.init(20, 20, -20 / 2, -3, -3, 1.1);

  /* Start */
  pEngine.run(cvs, camera, screen, map);
})();
