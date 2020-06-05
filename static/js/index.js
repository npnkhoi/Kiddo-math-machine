(function() {
    var createCanvas = function(canvasName) {
        var canvas = document.querySelector(canvasName);

        var context = canvas.getContext("2d");
        var Mouse = { x: 0, y: 0 };
        var lastMouse = { x: 0, y: 0 };
        
        canvas.width = 200;
        canvas.height = 200;
        context.clearRect(0, 0, 280, 280);
        context.fillStyle = "white";
        context.fillRect(0, 0, canvas.width, canvas.height);
        context.color = "black";
        context.lineWidth = 10;
        context.lineJoin = context.lineCap = 'round';

        canvas.addEventListener("mousemove", function (e) {
            lastMouse.x = Mouse.x;
            lastMouse.y = Mouse.y;

            Mouse.x = e.pageX - this.offsetLeft;
            Mouse.y = e.pageY - this.offsetTop;
        }, false);

        canvas.addEventListener("mousedown", function (e) {
            canvas.addEventListener("mousemove", onPaint, false);
        }, false);

        canvas.addEventListener("mouseup", function () {
            canvas.removeEventListener("mousemove", onPaint, false);
        }, false);

        var onPaint = function () {
            context.lineWidth = context.lineWidth;
            context.lineJoin = "round";
            context.lineCap = "round";
            context.strokeStyle = context.color;

            context.beginPath();
            context.moveTo(lastMouse.x, lastMouse.y);
            context.lineTo(Mouse.x, Mouse.y);
            context.closePath();
            context.stroke();
        };

        return canvas;
    }
    
    canvasLeft = createCanvas("#left_canvas");
    canvasMiddle = createCanvas("#middle_canvas");
    canvasRight = createCanvas("#right_canvas");
    
    debug();

    function debug() {
        $("#clearButton").on("click", function() {
            var img_left = canvasLeft.toDataURL('image/jpeg');
            console.log(img_left);

            var context = canvasLeft.getContext("2d");
            context.clearRect( 0, 0, 280, 280 );
            context.fillStyle = "white";
            context.fillRect(0, 0, canvasLeft.width, canvasLeft.height);

            var context = canvasMiddle.getContext("2d");
            context.clearRect(0, 0, 280, 280);
            context.fillStyle = "white";
            context.fillRect(0, 0, canvasMiddle.width, canvasMiddle.height);

            var context = canvasRight.getContext("2d");
            context.clearRect(0, 0, 280, 280);
            context.fillStyle = "white";
            context.fillRect(0, 0, canvasRight.width, canvasRight.height);
        });
    }
}());