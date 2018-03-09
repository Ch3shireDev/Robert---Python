import wpf

from System.Windows import Application, Window

class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'WpfApplication6.xaml')
    
    def Guzik_Click(self, sender, e):
        self.Licznik.Content = "ciasteczko"
    

if __name__ == '__main__':
    Application().Run(MyWindow())
