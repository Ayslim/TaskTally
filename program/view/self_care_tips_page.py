from PyQt5 import QtWidgets

from program.view.generated.GeneratedSelfCareTipsPage import Ui_Form

class SelfCareTipsPage(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.close_btn.clicked.connect(self.close)
        # self.tip1title.setText("You are the prize. Stop acting like you're the option.")
        # self.tip1label.setText("Reminder: Your time and energy are valuable. Prioritize tasks and people that align with your goals and well-being.")
        # self.tip2title.setText("You don't have to be perfect, you just have to try.")
        # self.tip2label.setText("Reminder: Progress is more important than perfection. Even small efforts count.")
        # self.tip3title.setText("Your life is a reflection of the standards you set for yourself.")
        # self.tip3label.setText("Reminder: Set realistic but meaningful goals for your day. You deserve a life that feels fulfilling.")

        ##the ones i added:
        #self.tip4_title.setText("Stop waiting for motivation. Discipline will take you further.")
        #self.tip4_label.setText("Reminder: Motivation comes and goes, but building small, consistent habits can help you stay on track.")
        #self.tip5_title.setText("You are not your past. You are not your mistakes. You are not what people say about you.")
        #self.tip5_label.setText("Reminder: Let go of guilt or shame about unfi nished tasks. Every day is a fresh start.")
        #self.tip6_title.setText("Protect your energy like your life depends on it, because it does.")
        #self.tip6_label.setText("Reminder: Say no to things that drain you, and make time for activities that recharge you.")
        #self.tip7_title.setText("You are allowed to take up space. You are allowed to exist unapologetically.")
        #self.tip7_label.setText("Reminder: Don't feel guilty for prioritizing your needs. Self-care isn't selfish, it is necessary.")
        #self.tip8_title.setText("The way you speak to yourself matters. Be kind to yourself.")
        #self.tip8_label.setText('Reminder: Replace negative self-talk with encouragement. Instead of “I cannot do this,” try “I will do my best.')
        #self.tip9_title.setText("Stop overthinking and start doing. Action will always beat fear.")
        #self.tip9_label.setText("Reminder: Overwhelmed by a task? Just start. Taking the fi rst step is often the hardest part.")

        self.previousPageBtn.clicked.connect(self.goPrevious)
        self.nextPageBtn.clicked.connect(self.goNext)

    def goPrevious(self):
        current_index = self.stackedWidget.currentIndex()
        if current_index > 0:
            self.stackedWidget.setCurrentIndex(current_index - 1)   

    def goNext(self):
        current_index = self.stackedWidget.currentIndex()
        if current_index < self.stackedWidget.count() - 1:
            self.stackedWidget.setCurrentIndex(current_index + 1)
       


