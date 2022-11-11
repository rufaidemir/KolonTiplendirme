import sys, os
import traceback
from PyQt5.QtWidgets import QApplication, QMainWindow, QSplashScreen, QProgressBar, QFileDialog, QMessageBox,QInputDialog, QLineEdit
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt, QSettings
import pandas
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from KolonTip.KolonTipGUI import Ui_MainWindow





class MainGUI(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow() 
        self.ui.setupUi(self)
        self.setWindowTitle(f"KOLON TİPLENDİRME")
        
        self.ui.pushButton_select_path.pressed.connect(self.selecExcelFilePath)
        self.settings = QSettings("RufaiDemir","kolTyperSettings")
        
        self.selecExcelFilePath =None
        
        
        
    
    
    def selecExcelFilePath(self):
        try:
            fileName, _ = QFileDialog.getOpenFileName(self,"Excel Seç",directory=self.settings.value("columnExcelPath", os.path.join(os.environ["HOMEPATH"], "Desktop")), filter="Excel Files (*.xlsx);;All Files (*)")
            if fileName:
                excelFile = pandas.ExcelFile(fileName)
                self.ui.comboBox_sheet_name_excel.clear()
                self.ui.comboBox_sheet_name_excel.addItems(excelFile.sheet_names)
                self.ui.comboBox_sheet_name_excel.setCurrentIndex(0)
                self.ui.lineEdit_path.setText(fileName)
                self.selecExcelFilePath = fileName
                
                self.reacExcelInfo()
        
        except Exception as e:
            self.ui.pushButton_select_path.setText("TİPLENDİR")
            QMainWindow.repaint(self)
            print(traceback.format_exc())
            QMessageBox.warning(self,"HATA","Excel doyası oluşturulurken veya açılırken bir hata alındı. Hata: "+str(e))
                

    def reacExcelInfo(self):
        df = pandas.read_excel(self.selecExcelFilePath, sheet_name=self.ui.comboBox_sheet_name_excel.currentText())
        
        self.ui.listWidget_all_columns.clear()
        self.ui.listWidget_all_columns.addItems(list(df))
        
        self.ui.comboBox_section_name.clear()
        self.ui.comboBox_section_name.addItems(list(df))
        self.ui.comboBox_section_name.setCurrentIndex(0)
        
        print(df)
        
 
 
if __name__ =='__main__':
    app =QApplication(sys.argv)
    app.setStyle('Fusion')
 
    app.processEvents()
    window =MainGUI()
    window.show()

    app.exec_()