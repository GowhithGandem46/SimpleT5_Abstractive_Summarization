import os
import time
from turtle import pu
from simplet5 import SimpleT5
from pywebio.input import *
from pywebio.output import *

class App:

    def __init__(self) -> None:
        self.model = SimpleT5()
        self.model.load_model("t5","C:\\Users\\eruku\\Documents\\summary\\krupa",use_gpu=False)
        os.system("cls")
    
    def bar(self):
        time.sleep(3)
        put_loading().style('width:4rem; height:4rem')

    def display(self):
        res = textarea('Enter Text For Summarization')
        #self.bar()
        summary = self.model.predict(str(res))[0]
        if len(summary)!=0:
            myvar=True
        #put_loading().style('width:4rem; height:4rem')
        '''if myvar==True:
            with put_loading().style('width:4rem; height:4rem'):
                time.sleep(3)
                put_text('Welcome to Summary Test')'''
        put_text('Given Text:')
        put_text(res)
        put_text(' ')
        put_text('Analysis:')
        ratio = 100-((len(summary)/len(res))*100)
        put_table([
            ['No of words in given text :',put_text(str(len(res.split(' '))))],
            ['No of words in summary :',put_text(str(len(summary.split(' '))))],
            ['Optimisation percentage :',put_text(str(ratio))]
        ]
        )
        put_text(' ')
        put_text("Summary Text")
        put_text(summary)
        


run = App()
run.display()