from PyQt5.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtCore import Qt
import pandas as pd

class TableDisplay(QMainWindow):
    def __init__(self, df):
        super().__init__()

        self.df = df

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.tableWidget = QTableWidget()
        self.layout.addWidget(self.tableWidget)

        self.setup_table()

        self.sort_button = QPushButton("Sort Market Cap")
        self.sort_button.clicked.connect(self.sort_market_cap)
        self.layout.addWidget(self.sort_button)

    def setup_table(self):
        # Set the number of rows and columns
        self.tableWidget.setRowCount(self.df.shape[0])
        self.tableWidget.setColumnCount(self.df.shape[1])

        # Set the column headers
        self.tableWidget.setHorizontalHeaderLabels(self.df.columns)

        # Enable sorting
        self.tableWidget.setSortingEnabled(True)

        # Populate the table with data
        for row_idx, row_data in self.df.iterrows():
            for col_idx, cell_data in enumerate(row_data):

                item = QTableWidgetItem()
                if pd.isna(cell_data):
                    cell_data = -1
                elif self.df.columns[col_idx] == "marketCap":
                    item.setData(Qt.DisplayRole, cell_data / 1e9)
                else:
                    item.setData(Qt.DisplayRole, cell_data)

                # Set item flags to make it non-editable
                item.setFlags(item.flags() ^ Qt.ItemIsEditable)
                self.tableWidget.setItem(row_idx, col_idx, item)

        # Adjust column widths to fit the content
        self.tableWidget.resizeColumnsToContents()

    def sort_market_cap(self):
        # Sort DataFrame by Market Cap in ascending order (string comparison)
        self.df['Market Cap'] = self.df['Market Cap'].astype(str)
        self.df.sort_values(by='Market Cap', ascending=True, inplace=True)
        # Repopulate the table with sorted data
        self.setup_table()
