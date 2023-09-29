import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication
from ui import TableDisplay
from snp500 import get_snp500_data

def main():

    df = get_snp500_data()

    app = QApplication(sys.argv)
    window = TableDisplay(df)
    window.setWindowTitle('주식 분석 테이블')
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
