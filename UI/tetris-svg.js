"use strict";
window.addEventListener("load", function (ev) {
    // SVG UI for Tetris
    var opt = {
        svgid: "stage",
        svgns: "http://www.w3.org/2000/svg",
        scale: 24,
        width: 10,
        height: 20,
    };

    var newBlock = function () {
        return Tetris.Block(
            0|(opt.width / 2) - 2, 0, 0,
            Tetris.shapes[0|(Math.random() * Tetris.shapes.length)]);
    };

    var render = function () {
        while (view.hasChildNodes()) view.removeChild(view.lastChild);
        stage.eachStone(function (x, y, color) {
            view.appendChild(stone(x, y, color));
        });
        block.eachStone(function (x, y, color) {
            view.appendChild(stone(x, y, color));
        });
        var score = Tetris.getScore();
        document.getElementById("score").innerHTML = score;
    };

    var stone = function (x, y, color) {
        var rect = document.createElementNS(opt.svgns, "rect");
        rect.setAttribute("x", opt.scale * x);
        rect.setAttribute("y", opt.scale * y);
        rect.setAttribute("width", opt.scale);
        rect.setAttribute("height", opt.scale);
        rect.setAttribute("fill", color);
        rect.setAttribute("stroke", "black");
        return rect;
    };

    var tryLeft = function () {
        var next = block.left();
        if (!next.ok(stage)) return;
        block = next;
        render();
    };
    var tryRight = function () {
        var next = block.right();
        if (!next.ok(stage)) return;
        block = next;
        render();
    };
    var tryRotate = function () {
        var next = block.rotate();
        if (!next.ok(stage)) return;
        block = next;
        render();
    };
    var tryFall = function () {
        var next = block.fall();
        if (next.ok(stage)) {
            block = next;
            return render();
        } else {
            block.put(stage);
            render();
            setTimeout(function () {
                stage.shrink();
                block = newBlock();
                if (!block.ok(stage)) {
                    // gameover
                    stage.reset();
                }
                render();
            }, 10);
        }
    };

    var timer = function() {
        tryFall();
    };

    // init
    var view = document.getElementById(opt.svgid);
    view.setAttribute("width", opt.scale * opt.width);
    view.setAttribute("height", opt.scale * opt.height);
    view.style.backgroundColor = "white";

    var stage = Tetris.Stage(opt.width, opt.height);
    var block = newBlock();
    // not work keypress event on chrome svg
    var keyHandler = function (ev) {
        //console.log(ev.target);
        switch (ev.keyCode) {
            case 37: return tryLeft(); //left
            case 38: return tryRotate(); //up
            case 39: return tryRight(); //right
            case 40: return tryFall(); //down
        }
    };

    //view.addEventListener("keydown", keyHandler, false);
    document.body.addEventListener("keydown", keyHandler, false);
    //window.addEventListener("keydown", keyHandler, false);
    render();

    setInterval(timer, 1000);

    timer();
}, false);
