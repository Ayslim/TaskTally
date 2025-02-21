# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'info.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_InfoPage(object):
    def setupUi(self, background):
        background.setObjectName("background")
        background.resize(1440, 900)

        # Back to menu button
        self.btn_menu = QtWidgets.QPushButton(background)
        self.btn_menu.setGeometry(QtCore.QRect(40, 40, 151, 41))
        self.btn_menu.setObjectName("btn_menu")
        self.btn_menu.setText("Back to menu")
        self.btn_menu.setStyleSheet(
            "QPushButton {\n"
            "    color: black;\n"
            "    border: 2px solid black;\n"
            "    border-radius: 5px;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: #d3d3d3;\n"
            "}\n"
            ""
        )
        self.btn_menu.clicked.connect(background.close)

        # Main label for the page
        self.info_page_label = QtWidgets.QLabel(background)
        self.info_page_label.setGeometry(QtCore.QRect(440, 80, 551, 81))
        self.info_page_label.setAlignment(QtCore.Qt.AlignCenter)
        self.info_page_label.setStyleSheet(
            "QLabel {\n"
            "    color: black;\n"
            "    font-size: 48px;\n"
            "    font-style: italic;"
            "    font-weight: bold;"
            "    padding: 10px;\n"
            "    border-radius: 5px;\n"
            "    border: 2px solid black;\n"
            "}\n"
            ""
        )
        self.info_page_label.setObjectName("info_page_label")
        self.info_page_label.setText("Info Page")

        # The area where info text will be in
        self.textEdit = QtWidgets.QTextEdit(background)
        self.textEdit.setGeometry(QtCore.QRect(140, 210, 1181, 511))
        self.textEdit.setStyleSheet(
            "QTextEdit {\n"
            "    background-color: #ECECEC; \n"
            "    color: black;\n"
            "    border: 2px solid black;\n"
            "    border-radius: 5px;\n"
            "    padding: 10px;\n"
            "}\n"
            ""
        )
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(background)
        QtCore.QMetaObject.connectSlotsByName(background)
    
    # info text formatted
    def retranslateUi(self, background):
        _translate = QtCore.QCoreApplication.translate
        background.setWindowTitle(_translate("background", "Form"))

        self.textEdit.setHtml(
            _translate(
                "background",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Arial\'; font-weight:600; color:#000000;">TaskTally - Your Productivity &amp; Self-Care Companion</span></p>\n'
                "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Arial'; font-weight:600; color:#000000;\"><br /></p>\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Arial\'; font-weight:600; color:#000000;">About TaskTally</span></p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Arial\'; color:#000000;">TaskTally is designed to help individuals of all ages, from teenagers to senior citizens, plan their days effectively, stay motivated, and incorporate self-care into their routine. Many people struggle with prioritizing their mental health, which can lead to neglecting essential tasks. TaskTally aims to change that by promoting self-care and productivity together.</span></p>\n'
                "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Arial'; color:#000000;\"><br /></p>\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Arial\'; font-weight:600; color:#000000;">Features</span></p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Arial\'; color:#000000;">● </span><span style=" font-family:\'Arial\'; font-weight:600; color:#000000;">To-Do List</span><span style=" font-family:\'Arial\'; color:#000000;">: Easily add, organize, and check off tasks, including predefined self-care activities.</span></p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Arial\'; color:#000000;">● </span><span style=" font-family:\'Arial\'; font-weight:600; color:#000000;">Progress Tracking</span><span style=" font-family:\'Arial\'; color:#000000;">: Get insights into your efficiency and productivity over time.</span></p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Arial\'; color:#000000;">● </span><span style=" font-family:\'Arial\'; font-weight:600; color:#000000;">Motivational Tips &amp; Self-Care Messages</span><span style=" font-family:\'Arial\'; color:#000000;">: Receive supportive quotes, tips, and advice to boost inspiration.</span></p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Arial\'; color:#000000;">● </span><span style=" font-family:\'Arial\'; font-weight:600; color:#000000;">Statistics &amp; Insights</span><span style=" font-family:\'Arial\'; color:#000000;">: Visualize your progress and identify areas for improvement.</span></p>\n'
                "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Arial'; color:#000000;\"><br /></p>\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Arial\'; font-weight:600; color:#000000;">How to Use TaskTally</span></p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Arial\'; font-weight:600; color:#000000;">1.</span><span style=" font-family:\'Arial\'; color:#000000;"> </span><span style=" font-family:\'Arial\'; font-weight:600; color:#000000;">Navigate the Menu</span><span style=" font-family:\'Arial\'; color:#000000;">: Use the main menu to access different sections.</span></p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Arial\'; font-weight:600; color:#000000;">2. Manage Your Tasks</span><span style=" font-family:\'Arial\'; color:#000000;">: Add and complete tasks in the To-Do List section.</span></p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Arial\'; font-weight:600; color:#000000;">3. View Your Progress</span><span style=" font-family:\'Arial\'; color:#000000;">: Check the Statistics page to see how well you\'re doing.</span></p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Arial\'; font-weight:600; color:#000000;">4. Stay Motivated</span><span style=" font-family:\'Arial\'; color:#000000;">: Read useful productivity and self-care tips to boost your efficiency.</span></p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Arial\'; font-weight:600; color:#000000;">5. Earn Points</span><span style=" font-family:\'Arial\'; color:#000000;">: Complete tasks and accumulate points.</span></p>\n'
                "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Arial'; color:#000000;\"><br /></p>\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Arial\'; font-weight:600; color:#000000;">Ethical Aspects &amp; Social Responsibility</span></p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Arial\'; color:#000000;">● </span><span style=" font-family:\'Arial\'; font-weight:600; color:#000000;">Accessibility</span><span style=" font-family:\'Arial\'; color:#000000;">: TaskTally follows the </span><span style=" font-family:\'Arial\'; color:#103cc0;">Web Content Accessibility Guidelines (WCAG)</span><span style=" font-family:\'Arial\'; color:#000000;"> to ensure usability for all age groups.</span></p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Arial\'; color:#000000;">● </span><span style=" font-family:\'Arial\'; font-weight:600; color:#000000;">Data Transparency</span><span style=" font-family:\'Arial\'; color:#000000;">: Users will be informed about how their data is used.</span></p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Arial\'; color:#000000;">● </span><span style=" font-family:\'Arial\'; font-weight:600; color:#000000;">Reliable Information</span><span style=" font-family:\'Arial\'; color:#000000;">: Self-care tips will be backed by scientific evidence or credible sources. A disclaimer will clarify that TaskTally is not developed by mental health professionals.</span></p>\n'
                "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Arial'; color:#000000;\"><br /></p>\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Arial\'; font-weight:600; color:#000000;">Why Use TaskTally?</span></p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Arial\'; color:#000000;">● Encourages </span><span style=" font-family:\'Arial\'; font-weight:600; color:#000000;">self-care and mental well-being</span><span style=" font-family:\'Arial\'; color:#000000;">.</span></p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Arial\'; color:#000000;">● Helps with </span><span style=" font-family:\'Arial\'; font-weight:600; color:#000000;">daily planning</span><span style=" font-family:\'Arial\'; color:#000000;"> and </span><span style=" font-family:\'Arial\'; font-weight:600; color:#000000;">task management</span><span style=" font-family:\'Arial\'; color:#000000;">.</span></p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Arial\'; color:#000000;">● Encourages </span><span style=" font-family:\'Arial\'; font-weight:600; color:#000000;">productivity</span><span style=" font-family:\'Arial\'; color:#000000;"> and </span><span style=" font-family:\'Arial\'; font-weight:600; color:#000000;">habit-building</span><span style=" font-family:\'Arial\'; color:#000000;">.</span></p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Arial\'; color:#000000;">● Offers </span><span style=" font-family:\'Arial\'; font-weight:600; color:#000000;">insightful feedback</span><span style=" font-family:\'Arial\'; color:#000000;"> on your progress.</span></p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Arial\'; color:#000000;">● Provides </span><span style=" font-family:\'Arial\'; font-weight:600; color:#000000;">motivational support</span><span style=" font-family:\'Arial\'; color:#000000;"> to keep you on track.</span></p>\n'
                "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Arial'; color:#000000;\"><br /></p>\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Arial\'; font-weight:600; color:#000000;">Overview of System Architecture</span></p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Arial\'; color:#000000;">● </span><span style=" font-family:\'Arial\'; font-weight:600; color:#000000;">Main Menu</span></p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Arial\'; color:#000000;">● </span><span style=" font-family:\'Arial\'; font-weight:600; color:#000000;">Self-Care Tips</span></p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Arial\'; color:#000000;">● </span><span style=" font-family:\'Arial\'; font-weight:600; color:#000000;">To-Do List</span></p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Arial\'; color:#000000;">● </span><span style=" font-family:\'Arial\'; font-weight:600; color:#000000;">Statistics</span></p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Arial\'; color:#000000;">● </span><span style=" font-family:\'Arial\'; font-weight:600; color:#000000;">Info Page</span></p>\n'
                "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Arial'; font-weight:600; color:#000000;\"><br /></p>\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Arial\'; font-weight:600; color:#000000;">Contact &amp; Support</span></p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Arial\'; color:#000000;">If you have any questions, feedback, or need assistance, feel free to reach out to our support team at “</span><span style=" font-family:\'Arial\'; font-weight:600; color:#103cc0;">support@tasktally.com</span><span style=" font-family:\'Arial\'; color:#000000;">.” </span></p>\n'
                "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Arial'; color:#000000;\"><br /></p>\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Arial\'; color:#000000;">Start your journey toward better productivity and self-care with TaskTally today!</span> </p></body></html>',
            )
        )


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    background = QtWidgets.QWidget()
    ui = Ui_InfoPage()
    ui.setupUi(background)
    background.show()
    sys.exit(app.exec_())
