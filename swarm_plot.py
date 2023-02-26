import matplotlib.pyplot as plt
import numpy as np
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-i', '--input_file', default='BME163_Input_Data_3.txt')
parser.add_argument('-o', '--output_file', default='Aldapa_Alberto_BME163_Assignment_Week44.png')
parser.add_argument('-s', '--style_sheet', default='BME163.mplstyle') # BME163

args = parser.parse_args()

inputFile = open(args.input_file, 'r')
outputFile = args.output_file
styleSheet = args.style_sheet

plt.style.use(styleSheet)

figureHeight = 3
figureWidth = 7

plt.figure(figsize=(figureWidth, figureHeight))

panelWidth = 5
panelHeight = 2

relativePanelWidth = panelWidth/figureWidth
relativePanelHeight = panelHeight/figureHeight

panel1 = plt.axes([.1, 0.2, relativePanelWidth, relativePanelHeight])

pointDictionary = {}

for line in inputFile:
    splitLine = line.strip().replace('-', '_').replace('\t', '_').split('_')
    group = int(splitLine[7])
    if group >= 11:
        group = 11
    yValue = float(splitLine[15])
    if group not in pointDictionary:
        pointDictionary[group] = []
    pointDictionary[group].append(yValue)


def swarmplot(panel1, yList, x, panelWidth, panelHeight, xMin, xMax, yMax, yMin, markerSize):

    plottedPointsR = []
    plottedPointsL = []

    panel1.plot(x, yList[0],
                marker='o',
                markerfacecolor=(0, 0, 0),
                markeredgecolor='black',
                markersize=markerSize,
                markeredgewidth=0,
                linewidth=0)

    plottedPointsR.append((x, yList[0]))
    plottedPointsL.append((x, yList[0]))
    yList = np.delete(yList, 0, 0)

    xRange = xMax - xMin
    yRange = yMax - yMin

    for y in yList:
        printed = False
        shift = 0
        while not printed:
            hitR = False
            for otherPointR in plottedPointsR:
                if y != otherPointR[1]:
                    xDistInchR = ((((x + shift) - otherPointR[0]) / xRange) * panelWidth)
                    yDistInchR = (((y - otherPointR[1]) / yRange) * panelHeight)
                    markerSizeInches = markerSize / 72
                    distanceR = np.sqrt(xDistInchR ** 2 + yDistInchR ** 2)
                    if distanceR <= markerSizeInches:
                        hitR = True
                        hitL = False
                        for otherPointL in plottedPointsL:
                            if y != otherPointL[1]:
                                xDistInchL = ((((x - shift) - otherPointL[0]) / xRange) * panelWidth)
                                yDistInchL = (((y - otherPointL[1]) / yRange) * panelHeight)
                                distanceL = np.sqrt(xDistInchL ** 2 + yDistInchL ** 2)
                                if distanceL <= markerSizeInches:
                                    hitL = True
                                    break
                        if not hitL:
                            panel1.plot(x - shift, y,
                                        marker='o',
                                        markerfacecolor=(0, 0, 0),
                                        markeredgecolor='black',
                                        markersize=markerSize,
                                        markeredgewidth=0,
                                        linewidth=0)
                            if shift == 0:
                                plottedPointsR.append((x, y))
                                plottedPointsL.append((x, y))
                            plottedPointsL.append((x - shift, y))
                            printed = True
                            break
                        else:
                            break
            if not hitR:
                panel1.plot(x + shift, y,
                            marker='o',
                            markerfacecolor=(0, 0, 0),
                            markeredgecolor='black',
                            markersize=markerSize,
                            markeredgewidth=0,
                            linewidth=0)
                if shift == 0:
                    plottedPointsR.append((x, y))
                    plottedPointsL.append((x, y))
                plottedPointsR.append((x + shift, y))
                printed = True
            else:
                shift += markerSizeInches / 3
    width = .8
    median = np.median(yList)
    panel1.plot([x - width / 2, x + width / 2], [median, median],
                linewidth=1, color='red')


for key in pointDictionary:
    x = key
    yList = np.random.choice(pointDictionary[x], 1000)
    xMin = 0
    xMax = 12
    yMin = 75
    yMax = 100
    markerSize = .7

    swarmplot(panel1, yList, x, panelWidth, panelHeight, xMin, xMax, yMax, yMin, markerSize)

xval = np.linspace(0, 12.5, 600)
yval = np.linspace(95, 95, 600)
panel1.plot(xval, yval, dashes=[2, 2, 1, 2], color='black', linewidth=.5)

panel1.set_ylim(75, 100)
panel1.set_xlim(.25, 11.75)
panel1.set_xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
panel1.set_xticklabels(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '>11'])

panel1.set_xlabel(r'Subread Coverage', fontsize=8.0)
panel1.set_ylabel(r'Identity %', fontsize=8.0)

plt.savefig(outputFile, dpi=600)
