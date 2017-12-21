/**
 * Created by hp on 2017/12/20.
 */
    function radio(){
        var cv = document.getElementById("1");
        var cvx = cv.getContext("2d");
        var str;
        var math;
        cvx.translate(800,600);
        for (i = 0;i <= 7;i++) {
            str = "rgb(" + (30*i) + "," + (300-30*i) + ",50)";
            cvx.fillStyle = str;
            cvx.strokeStyle = str;
            cvx.arc(0, -60, 15, 0, Math.PI, true);
            cvx.fill();
            cvx.closePath();
            cvx.moveTo(0,-60);
            cvx.lineTo(0,-30);
            cvx.moveTo(0,-30);
            cvx.arc(-5,-30,5,0,Math.PI,false);
            cvx.stroke();
            cvx.rotate(Math.PI/4);
            cvx.beginPath();
            cvx.moveTo(15,-60);
        }
    }