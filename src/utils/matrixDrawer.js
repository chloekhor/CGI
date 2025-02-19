// src/utils/matrixDrawer.js

export function drawMatrix(canvasRef, targetValues, evaluationResult) {
    if (!canvasRef) return;

    const canvas = canvasRef;
    const ctx = canvas.getContext("2d");

    ctx.clearRect(0, 0, canvas.width, canvas.height);

    const centerX = canvas.width / 2;
    const centerY = canvas.height / 2;
    const scale = 19.5; 

    ctx.strokeStyle = "black";
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(centerX, 0);
    ctx.lineTo(centerX, canvas.height);
    ctx.moveTo(0, centerY);
    ctx.lineTo(canvas.width, centerY);
    ctx.stroke();

    let targetPoints = { left: null, right: null, top: null, bottom: null };
    let resultPoints = { left: null, right: null, top: null, bottom: null };

    // target
    if (targetValues) {
        ctx.fillStyle = "black";
        const targetCoords = {
            top: { value: targetValues[1], x: centerX, y: centerY - targetValues[1] * scale },
            left: { value: targetValues[0], x: centerX - targetValues[0] * scale, y: centerY },
            right: { value: targetValues[2], x: centerX + targetValues[2] * scale, y: centerY },
            bottom: { value: targetValues[3], x: centerX, y: centerY + targetValues[3] * scale }
        };

        Object.keys(targetCoords).forEach((key) => {
            const { value, x, y } = targetCoords[key];
            if (value !== 0) {
                drawPoint(ctx, x, y);
                targetPoints[key] = { x, y };
            }
        });

        drawCrossLines(ctx, targetPoints, "black");
    }

    // AI result
    if (evaluationResult) {
        ctx.fillStyle = "red";
        const resultCoords = {
            top: { value: evaluationResult.Informative, x: centerX, y: centerY - evaluationResult.Informative * scale },
            left: { value: evaluationResult.Remunerative, x: centerX - evaluationResult.Remunerative * scale, y: centerY },
            right: { value: evaluationResult.Relational, x: centerX + evaluationResult.Relational * scale, y: centerY },
            bottom: { value: evaluationResult.Entertainment, x: centerX, y: centerY + evaluationResult.Entertainment * scale }
        };

        Object.keys(resultCoords).forEach((key) => {
            const { value, x, y } = resultCoords[key];
            if (value !== 0) {
                drawPoint(ctx, x, y);
                resultPoints[key] = { x, y };
            }
        });

        drawCrossLines(ctx, resultPoints, "red");
    }
}

function drawCrossLines(ctx, points, color) {
    ctx.strokeStyle = color;
    ctx.lineWidth = 2;
    ctx.setLineDash([5, 5]); 

    const activePoints = Object.values(points).filter(point => point !== null);

    if (activePoints.length === 4) {
        drawLine(ctx, points.left.x, points.left.y, points.top.x, points.top.y);
        drawLine(ctx, points.right.x, points.right.y, points.top.x, points.top.y);
        drawLine(ctx, points.left.x, points.left.y, points.bottom.x, points.bottom.y);
        drawLine(ctx, points.right.x, points.right.y, points.bottom.x, points.bottom.y);
    } else if (activePoints.length === 3) {
        drawPolygon(ctx, activePoints);
    } else if (activePoints.length === 2) {
        drawLine(ctx, activePoints[0].x, activePoints[0].y, activePoints[1].x, activePoints[1].y);
    }

    ctx.setLineDash([]); 
}

function drawPolygon(ctx, points) {
    if (points.length !== 3) return;
    ctx.beginPath();
    ctx.moveTo(points[0].x, points[0].y);
    ctx.lineTo(points[1].x, points[1].y);
    ctx.lineTo(points[2].x, points[2].y);
    ctx.closePath();
    ctx.stroke();
}

function drawLine(ctx, x1, y1, x2, y2) {
    ctx.beginPath();
    ctx.moveTo(x1, y1);
    ctx.lineTo(x2, y2);
    ctx.stroke();
}

function drawPoint(ctx, x, y) {
    ctx.beginPath();
    ctx.arc(x, y, 5, 0, Math.PI * 2);
    ctx.fill();
}
