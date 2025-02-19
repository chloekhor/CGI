import { jsPDF } from "jspdf";
import autoTable from "jspdf-autotable";

export function generatePDFReport(evaluationResult, targetValues, recommendation, canvasRef, photoUrl) {
  const doc = new jsPDF("p", "mm", "a4");
  const pageHeight = doc.internal.pageSize.height;
  const pageWidth = doc.internal.pageSize.width;
  let yOffset = 20;

  doc.setFontSize(18);
  const titleText = "AI Evaluation Report";
  const textWidth = doc.getTextWidth(titleText);
  const centerX = (pageWidth - textWidth) / 2;
  doc.text(titleText, centerX, yOffset);
  yOffset += 10;

  const loadImage = new Promise((resolve, reject) => {
    if (photoUrl) {
      const img = new Image();
      img.src = photoUrl;
      img.crossOrigin = "Anonymous";
      img.onload = () => {
        const maxImgHeight = 80;
        let imgHeight = maxImgHeight;
        let imgWidth = (img.width / img.height) * imgHeight; 
  
  
        const imgX = (pageWidth - imgWidth) / 2;
        doc.addImage(img, "JPEG", imgX, yOffset, imgWidth, imgHeight);
        yOffset += imgHeight + 10; 
  
        resolve();
      };
      img.onerror = reject;
    } else {
      resolve();
    }
  });
  
  
  // table
  loadImage.then(() => {
    doc.setFontSize(14);
    doc.text("Target Values vs AI Evaluation Scores", 15, yOffset);
    yOffset += 5;

    const dimensions = ["Remunerative", "Informative", "Relational", "Entertainment"];
    const tableData = dimensions.map((dim, index) => {
      const target = targetValues[index];
      const result = evaluationResult[dim] || 0;
      const status = target > result ? "Needs Improvement" : target === result ? "Achieved" : "Exceeded";
      return [dim, result, target, status];
    });

    autoTable(doc, {
      startY: yOffset,
      head: [["Dimension", "AI Score", "Target Score", "Status"]],
      body: tableData,
      theme: "grid",
      styles: { fontSize: 12, cellPadding: 4 },
      headStyles: { fillColor: [0, 102, 204], textColor: 255, fontStyle: "bold" },
      alternateRowStyles: { fillColor: [240, 240, 240] },
      margin: { top: 10, left: 15, right: 15 },
    });

      yOffset = doc.lastAutoTable.finalY + 10;

      // canva
      if (canvasRef) {
        const canvasDataUrl = canvasRef.toDataURL("image/png");
        const canvasWidth = 120;
        const canvasHeight = 120;
        const canvasX = (pageWidth - canvasWidth) / 2;
        const canvasY = yOffset;

        if (canvasY + canvasHeight > pageHeight - 20) {
          doc.addPage();
          yOffset = 20;
        }
        doc.addImage(canvasDataUrl, "PNG", canvasX, yOffset, canvasWidth, canvasHeight);

        const textPadding = 5; 

        doc.setFontSize(12);
        doc.text("Informative", canvasX + canvasWidth / 2 - 10, yOffset - textPadding); 
        doc.text("Entertainment", canvasX + canvasWidth / 2 - 12, yOffset + canvasHeight + textPadding + 5);
        doc.saveGraphicsState();
        doc.setFontSize(12);


        doc.text("Remunerative", canvasX - textPadding, yOffset + canvasHeight / 2 + 11, { angle: 90 });
        doc.text("Relational", canvasX + canvasWidth + textPadding, yOffset + canvasHeight / 2 -10, { angle: -90 });
        doc.restoreGraphicsState();

        yOffset += canvasHeight + 20;
      }

    
      // color tips
      doc.setFontSize(12);
      const legendTextBlack = "Target Values";
      const legendTextRed = "AI Evaluation Scores";
      const dotSize = 2;
      const spacing = 8;
      const gapBetweenLegends = 15;

      const textWidthBlack = doc.getTextWidth(legendTextBlack);
      const textWidthRed = doc.getTextWidth(legendTextRed);
      const totalWidth = textWidthBlack + textWidthRed + gapBetweenLegends + (dotSize * 4) + (spacing * 2);

      const startX = (pageWidth - totalWidth) / 2;
      const dotYOffset = yOffset - 2;

      doc.setFillColor(0, 0, 0);
      doc.circle(startX, dotYOffset, dotSize, "F");
      doc.setFont("helvetica", "bold");
      doc.setTextColor(0, 0, 0);
      doc.text(legendTextBlack, startX + dotSize + spacing, yOffset);

      const redCircleX = startX + textWidthBlack + dotSize + spacing + gapBetweenLegends;
      doc.setFillColor(255, 0, 0);
      doc.circle(redCircleX, dotYOffset, dotSize, "F");

      doc.setTextColor(255, 0, 0);
      doc.text(legendTextRed, redCircleX + dotSize + spacing, yOffset);

      yOffset += 15;

      if (yOffset + 20 > pageHeight - 20) {
        doc.addPage();
        yOffset = 20;
      }
      doc.setFontSize(16);
      doc.setFont("helvetica", "bold");
      doc.setTextColor(0, 0, 0);
      doc.text("Detailed Recommendation", 15, yOffset);
      yOffset += 10;

      doc.setFontSize(12);
      let recommendationText = recommendation
        .replace(/### \*\*(.*?)\*\*/g, "$1")
        .replace(/#/g, "")
        .replace(/---/g, "")
        .trim();

      const boldMatches = recommendationText.match(/\*\*(.*?)\*\*/g) || [];
      let processedText = recommendationText;
      boldMatches.forEach(match => {
        const boldText = match.replace(/\*\*/g, ""); 
        processedText = processedText.replace(match, `[[BOLD]]${boldText}[[/BOLD]]`);
      });

      const recommendationLines = processedText.split("\n");

      recommendationLines.forEach(line => {
        const wrappedLines = doc.splitTextToSize(line, 180);

        wrappedLines.forEach(wrappedLine => {
          if (wrappedLine.includes("[[BOLD]]")) {
            const parts = wrappedLine.split("[[BOLD]]");
            let xPosition = 15;

            parts.forEach(part => {
              if (part.includes("[[/BOLD]]")) {
                const boldPart = part.split("[[/BOLD]]")[0];
                doc.setFont("helvetica", "bold");
                doc.text(boldPart, xPosition, yOffset);
                xPosition += doc.getTextWidth(boldPart);
                doc.setFont("helvetica", "normal");
                doc.text(part.split("[[/BOLD]]")[1], xPosition, yOffset);
                xPosition += doc.getTextWidth(part.split("[[/BOLD]]")[1]);
              } else {
                doc.text(part, xPosition, yOffset);
                xPosition += doc.getTextWidth(part);
              }
            });

            yOffset += 7;
          } else {
            doc.text(wrappedLine, 15, yOffset);
            yOffset += 7;
          }

          if (yOffset > pageHeight - 20) {
            doc.addPage();
            yOffset = 20;
          }
        });
      });

    doc.save("AI_Evaluation_Report.pdf");
  }).catch(error => {
    console.error("Error loading image:", error);
    doc.save("Evaluation_Report.pdf");
  });
}
