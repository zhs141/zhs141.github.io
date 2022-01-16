<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Rembound.com Example</title>
<script type="text/javascript" src="script.js"></script>
</head>
<body>
<canvas id="viewport" width="640" height="480"></canvas>
</body>
</html>
//窗口加载完成后调用
window.onload = function() {
    // 获取画布及context（上下文）
    var canvas = document.getElementById("viewport"); 
    var context = canvas.getContext("2d");
 
    // 记录时间帧，这个最好通过单步调试来理解
    var lastframe = 0;
    var fpstime = 0;
    var framecount = 0;
    var fps = 0;
 
    // 初始化游戏，添加鼠标的监听事件
    function init() {
        canvas.addEventListener("mousemove", onMouseMove);
        canvas.addEventListener("mousedown", onMouseDown);
        canvas.addEventListener("mouseup", onMouseUp);
        canvas.addEventListener("mouseout", onMouseOut);
 
        // 进入游戏主循环
        main(0);
    }
 
    // 主循环
    function main(tframe) {
        // 结束时继续调用main函数
        window.requestAnimationFrame(main);
 
        // 更新游戏
        update(tframe);
        render();
    }
 
    // 更新游戏状态，计算已经过去了的时间
    function update(tframe) {
        var dt = (tframe - lastframe) / 1000;
        lastframe = tframe;
 
        //更新帧数计数器
        updateFps(dt);
    }
 
    function updateFps(dt) {
        if (fpstime > 0.25) {
            //计算帧数
            fps = Math.round(framecount / fpstime);
 
            //重置时间
            fpstime = 0;
            framecount = 0;
        }
 
        //增加帧时间、帧数
        fpstime += dt;
        framecount++;
    }
 
    // 渲染（更新画布）
    function render() {
        drawFrame();
    }
 
    // 
    function drawFrame() {
        // 背景、边界
        context.fillStyle = "#d0d0d0";
        context.fillRect(0, 0, canvas.width, canvas.height);
        context.fillStyle = "#e8eaec";
        context.fillRect(1, 1, canvas.width-2, canvas.height-2);
 
        // 标题头
        context.fillStyle = "#303030";
        context.fillRect(0, 0, canvas.width, 65);
 
        // 标题
        context.fillStyle = "#ffffff";
        context.font = "24px Verdana";
        context.fillText("HTML5 Canvas Basic Framework - Rembound.com", 10, 30);
 
        // 显示帧数
        context.fillStyle = "#ffffff";
        context.font = "12px Verdana";
        context.fillText("Fps: " + fps, 13, 50);
    }
 
    //鼠标监听
    function onMouseMove(e) {}
    function onMouseDown(e) {}
    function onMouseUp(e) {}
    function onMouseOut(e) {}
 
    // 获取鼠标位置
    function getMousePos(canvas, e) {
        var rect = canvas.getBoundingClientRect();
        return {
            x: Math.round((e.clientX - rect.left)/(rect.right - rect.left)*canvas.width),
            y: Math.round((e.clientY - rect.top)/(rect.bottom - rect.top)*canvas.height)
        };
    }
 
    // 游戏入口
    init();
};
    var framecount = 0;
    var fps = 0;
 
    // 游戏平面
    var level = {
        x: 1,
        y: 65,
        width: canvas.width - 2,
        height: canvas.height - 66
    };
    
    // 小方块
    var square = {
        x: 0,
        y: 0,
        width: 0,
        height: 0,
        xdir: 0,
        ydir: 0,
        speed: 0
    }
    // 分数
    var score = 0;
    // 初始化游戏，添加鼠标的监听事件
    function init() {
        canvas.addEventListener("mouseout", onMouseOut);
         // 初始化方块
        square.width = 100;
        square.height = 100;
        square.x = level.x + (level.width - square.width) / 2;
        square.y = level.y + (level.height - square.height) / 2;
        square.xdir = 1;
        square.ydir = 1;
        square.speed = 200;
        
        // 初始化分数
        score = 0;
    
        // 进入游戏主循环
        main(0);

       //更新帧数计数器
        updateFps(dt);

       // 基于时间移动方块
        square.x += dt * square.speed * square.xdir;
        square.y += dt * square.speed * square.ydir;
        
        // 处理碰撞
        if (square.x <= level.x) {
            // Left edge
            square.xdir = 1;
            square.x = level.x;
        } else if (square.x + square.width >= level.x + level.width) {
            // Right edge
            square.xdir = -1;
            square.x = level.x + level.width - square.width;
        }

        if (square.y <= level.y) {
            // Top edge
            square.ydir = 1;
            square.y = level.y;
        } else if (square.y + square.height >= level.y + level.height) {
            // Bottom edge
            square.ydir = -1;
            square.y = level.y + level.height - square.height;
        }    

        // 绘制方块
        context.fillStyle = "#ff8080";
        context.fillRect(square.x, square.y, square.width, square.height);
        
        // 绘制内部
        context.fillStyle = "#ffffff";
        context.font = "38px Verdana";
        var textdim = context.measureText(score);
        context.fillText(score, square.x+(square.width-textdim.width)/2, square.y+65);
    function onMouseDown(e) {
        // 获取鼠标位置
        var pos = getMousePos(canvas, e);
        
        // 检查是否碰到了方块
        if (pos.x >= square.x && pos.x < square.x + square.width &&
            pos.y >= square.y && pos.y < square.y + square.height) {
            
            // 增加分数
            score += 1;
            
            // 增加速度
            square.speed *= 1.1;
            
            // 随机给一个新的位置
            square.x = Math.floor(Math.random()*(level.x+level.width-square.width));
            square.y = Math.floor(Math.random()*(level.y+level.height-square.height));
            
            // 随机方向
            square.xdir = Math.floor(Math.random() * 2) * 2 - 1;
            square.ydir = Math.floor(Math.random() * 2) * 2 - 1;
        }
    }
