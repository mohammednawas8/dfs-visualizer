import typing
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, uic
from PyQt5.QtWidgets import QWidget

from helper import *
from visualizers import *

graph = {1: [2, 3], 2: [5, 6], 3: [7, 8], 5: [
            9], 6: [10], 7: [10], 8: [4, 9], 9: [12]}
        
G = buildGraphUI(graph)
selectedAlgorithm = None

class MyGUI(QMainWindow):

    selectedAlgorithm = ""

    def __init__(self):
        super().__init__()
        uic.loadUi("GUI.ui", self)
        self.setWindowTitle("Searching Visualizer")
        self.setGeometry(200,300,340,605)
        self.show()
        self.selectedAlgorithm = "None"

        # Hide the results labels
        self.txtExpandedNodes.hide()
        self.label_4.hide()
        self.txtFinalPath.hide()


        self.btnShowGraph.clicked.connect(self.showGraphPreivew)
        self.btnCloseGraph.clicked.connect(self.closeGraphPreview)
        self.checkboxDfs.clicked.connect(self.selectCheckboxDfs)
        self.checkboxLdfs.clicked.connect(self.selectCheckboxLdfs)
        self.checkboxIds.clicked.connect(self.selectCheckboxIds)
        self.btnStart.clicked.connect(self.startSearchingInGraph)

    def showGraphPreivew(self):
        colorMap = ['blue' for node in G]
        drawGraph(G,colorMap)
        showGraph()

    def closeGraphPreview(self):
        closeGraph()

    def selectCheckboxDfs(self):
        self.selectedAlgorithm = "DFS"
        self.checkboxLdfs.setChecked(False)
        self.checkboxIds.setChecked(False)
        self.txtFieldLimit.setEnabled(False)
    
    def selectCheckboxLdfs(self):
        self.selectedAlgorithm = "LDFS"
        self.txtFieldLimit.setEnabled(True)
        self.checkboxDfs.setChecked(False)
        self.checkboxIds.setChecked(False)

    def selectCheckboxIds(self):
        self.selectedAlgorithm = "IDS"
        self.checkboxDfs.setChecked(False)
        self.checkboxLdfs.setChecked(False)
        self.txtFieldLimit.setEnabled(True)

    def startSearchingInGraph(self):
        plt.close()

        # Show the results labels
        self.txtExpandedNodes.show()
        self.label_4.show()
        self.txtFinalPath.show()

        selectedAlgorithm = self.selectedAlgorithm
        start = int(self.textFieldStartNode.text())
        goal = int(self.textFieldGoalNode.text())


        if(selectedAlgorithm == "DFS"):
            startDfsVisualizer(graph,start,goal,self)
        
        if(selectedAlgorithm == "LDFS"):
            limit = int(self.txtFieldLimit.text())
            startLimitedDFSVisualizer(graph,start,goal,limit,self)
        
        if(selectedAlgorithm == "IDS"):
            depth = int(self.txtFieldLimit.text())
            startIteretiveVisualizer(graph,start,goal,depth,self)
        

def main():
    app = QApplication([])
    window = MyGUI()
    app.exec_()


main()
