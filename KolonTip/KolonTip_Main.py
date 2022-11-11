import sys, os
import traceback
from PyQt5.QtWidgets import QApplication, QMainWindow, QSplashScreen, QProgressBar, QFileDialog, QMessageBox,QInputDialog, QLineEdit
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt, QSettings
import pandas
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from KolonTip.KolonTipGUI import Ui_MainWindow

from KolonTip.KolonTiplendirme import KolonTiplendirme





class MainGUI(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow() 
        self.ui.setupUi(self)
        self.setWindowTitle(f"KOLON TİPLENDİRME")
        
        self.ui.pushButton_select_path.pressed.connect(self.selecExcelFilePath)
        self.ui.pushButton_make_typing.pressed.connect(self.makeTypeExcel)
        self.settings = QSettings("RufaiDemir","kolTyperSettings")
        
        self.selecExcelFilePath =None
        self.df = pandas.DataFrame()
    
        
        
    def selecExcelFilePath(self):
        try:
            fileName, _ = QFileDialog.getOpenFileName(self,"Excel Seç",directory=self.settings.value("columnExcelPath", os.path.join(os.environ["HOMEPATH"], "Desktop")), filter="Excel Files (*.xlsx);;All Files (*)")
            if fileName:
                excelFile = pandas.ExcelFile(fileName)
                self.ui.comboBox_sheet_name_excel.disconnect()
                
                self.ui.comboBox_sheet_name_excel.clear()
                self.ui.comboBox_sheet_name_excel.addItems(excelFile.sheet_names)
                self.ui.comboBox_sheet_name_excel.setCurrentIndex(0)
                self.ui.lineEdit_path.setText(fileName)
                self.selecExcelFilePath = fileName

                self.ui.comboBox_sheet_name_excel.currentTextChanged.connect(self.readExcelInfo)
                self.readExcelInfo()
        
        except Exception as e:
            self.ui.pushButton_make_typing.setText("TİPLENDİR")
            QMainWindow.repaint(self)
            print(traceback.format_exc())
            QMessageBox.warning(self,"HATA","Excel okunurken veya açılırken bir hata alındı. Hata: "+str(e))
                

    def readExcelInfo(self):
        #read excelFile
        df = pandas.read_excel(self.selecExcelFilePath, sheet_name=self.ui.comboBox_sheet_name_excel.currentText())
        # add columns to widget
        self.ui.listWidget_all_columns.clear()
        self.ui.listWidget_selectted_columns_for_typing.clear()
        self.ui.listWidget_all_columns.addItems(list(df))
        
        # add columns to main id 
        self.ui.comboBox_section_name.clear()
        self.ui.comboBox_section_name.addItems(list(df))
        self.ui.comboBox_section_name.setCurrentIndex(0)

        self.df = df


    def makeTypeExcel(self):
        if self.ui.listWidget_selectted_columns_for_typing.count()>0:
            otherColumns = [self.ui.listWidget_selectted_columns_for_typing.item(i).text() for i in range(self.ui.listWidget_selectted_columns_for_typing.count())]
            allColumns = [self.ui.listWidget_all_columns.item(i).text() for i in range(self.ui.listWidget_all_columns.count())]
                
            param1 = self.ui.comboBox_section_name.currentText()
            typer = KolonTiplendirme(self.df, param1=param1, otherColumns=otherColumns)
            fileName, _ = QFileDialog.getSaveFileName(self,"Kaydet",directory=self.settings.value("columnTyperExcelPath", os.path.join(os.environ["HOMEPATH"], "Desktop")),filter="Excel Files (*.xlsx);;All Files (*)")
            self.settings.setValue("columnTyperExcelPath", os.path.dirname(fileName))
            
            saveDf = typer.getTypedDf 
            saveDf.to_excel(fileName)   
        else:
            QMessageBox.warning(self,"UYARI","Excel doyası oluşturmak için hangi kolonlara göre tiplendirme yapılacağı seçilmeli!")
        
 
 
if __name__ =='__main__':
    app =QApplication(sys.argv)
    app.setStyle('Fusion')
 
    app.processEvents()
    window =MainGUI()
    window.show()

    app.exec_()