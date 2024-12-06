"""
# TableReplay class for texas hold'em.
# Class displays 6-max table, along with hole cards and betting chips
"""

import tkinter as tk
import os

class TableReplay(tk.Canvas):
    
    pos_str = ('BN','SB','BB','EP','MP','CO')
    suits = {'c': '#00A318', 's': '#000000', 'h': '#FF3333', 'd': '#0093FB'}
    
    # coordinates for placing objects on table
    chippos_x = (205,360,500,505,350,198)
    chippos_y = (140,110,142,235,265,240)
    btn_x = (155,315,575,559,415,179)
    btn_y = (160,105,160,285,309,289)
    labelpos_x = (162,447,629,634,343,161)
    labelpos_y = (143,75,143,304,397,304)
        
    def __init__(self, parent, heropos, vilpos, situation_index, herocards, bet_size, theme, **kwargs):

        tk.Canvas.__init__(self, parent, width=765, height=440, bg=theme.bgcolor, highlightbackground=theme.bgcolor, highlightcolor=theme.bgcolor, highlightthickness=0, bd=0)

        # defines the preflop situation/positions
        self.heropos = heropos
        self.vilpos = vilpos
        self.situation_index = situation_index
        self.herocards = herocards
        self.bet_size = bet_size
        
        # define images
        img_dir = f'{os.getcwd()}\\Images'
        if theme.bgcolor == "#FFFFFF":
            self.ptable = tk.PhotoImage(file = f'{img_dir}\\handreplayer_table_med_default.png')
        else:
            self.ptable = tk.PhotoImage(file = f'{img_dir}\\handreplayer_table_med_dark.png')
        self.bn_marker = tk.PhotoImage(file = f'{img_dir}\\bn_marker.png')
        self.chips_sb = tk.PhotoImage(file = f'{img_dir}\\chips_sb.png')
        self.chips_bb = tk.PhotoImage(file = f'{img_dir}\\chips_bb.png')
        self.chips_2p25bb = tk.PhotoImage(file = f'{img_dir}\\chips_2p25bb.png')
        self.chips_2p5bb = tk.PhotoImage(file = f'{img_dir}\\chips_2p5bb.png')
        self.chips_3bb = tk.PhotoImage(file = f'{img_dir}\\chips_3bb.png')
        self.chips_7p5bb = tk.PhotoImage(file = f'{img_dir}\\chips_7p5bb.png')
        self.chips_8bb = tk.PhotoImage(file = f'{img_dir}\\chips_8bb.png')
        self.chips_9bb = tk.PhotoImage(file = f'{img_dir}\\chips_9bb.png')
        self.chips_11bb = tk.PhotoImage(file = f'{img_dir}\\chips_11bb.png')
        self.chips_12p5bb = tk.PhotoImage(file = f'{img_dir}\\chips_12p5bb.png')
        self.chips_13p5bb = tk.PhotoImage(file = f'{img_dir}\\chips_13p5bb.png')
        self.chips_20bb = tk.PhotoImage(file = f'{img_dir}\\chips_20bb.png')
        self.chips_23bb = tk.PhotoImage(file = f'{img_dir}\\chips_23bb.png')
        self.chips_26p5bb = tk.PhotoImage(file = f'{img_dir}\\chips_26p5bb.png')
        self.suit_h = tk.PhotoImage(file = f'{img_dir}\\suit_h.png')
        self.suit_d = tk.PhotoImage(file = f'{img_dir}\\suit_d.png')
        self.suit_c = tk.PhotoImage(file = f'{img_dir}\\suit_c.png')
        self.suit_s = tk.PhotoImage(file = f'{img_dir}\\suit_s.png')
        self.blank = tk.PhotoImage(file = f'{img_dir}\\blank.png')
        
        # draw table template
        self.grid(row=0, column=0, sticky='w')
        self.create_image(10, 10, anchor='nw', image=self.ptable)
        
        # draw position labels
        heropos_idx = TableReplay.pos_str.index(self.heropos)
        self.poslabels = []
        for i, pos in enumerate(TableReplay.pos_str):
            strdraw_idx = (heropos_idx + 2 + i) % len(TableReplay.pos_str)
            self.poslabels.append(self.create_text(TableReplay.labelpos_x[i], TableReplay.labelpos_y[i], text=TableReplay.pos_str[strdraw_idx], anchor='e', font=("Helvetica", 16, 'bold'), fill='white'))

        # post sb and bb and btn marker
        strdraw_idx = (5 - heropos_idx) % len(TableReplay.pos_str)
        self.sb_img = self.create_image(TableReplay.chippos_x[strdraw_idx], TableReplay.chippos_y[strdraw_idx], anchor='nw', image=self.chips_sb)
        strdraw_idx = (6 - heropos_idx) % len(TableReplay.pos_str)
        self.bb_img = self.create_image(TableReplay.chippos_x[strdraw_idx], TableReplay.chippos_y[strdraw_idx], anchor='nw', image=self.chips_bb)
        strdraw_idx = (4 - heropos_idx) % len(TableReplay.pos_str)
        self.btn_img = self.create_image(TableReplay.btn_x[strdraw_idx], TableReplay.btn_y[strdraw_idx], anchor='nw', image=self.bn_marker)
        
        self.itemconfigure(self.sb_img, state='hidden')
        self.itemconfigure(self.bb_img, state='hidden')
        self.itemconfigure(self.btn_img, state='hidden')

        # place bet amounts depending on preflop situation
        vilpos_idx = TableReplay.pos_str.index(self.vilpos)
        if self.situation_index == 1:
            strdraw_idx = (vilpos_idx + 4 - heropos_idx) % 6
            if self.vilpos in ['MP', 'EP']:
                self.vilchips_img = self.create_image(TableReplay.chippos_x[strdraw_idx], TableReplay.chippos_y[strdraw_idx], anchor = 'nw', image=self.chips_2p25bb)
            elif self.vilpos == 'SB':
                self.vilchips_img = self.create_image(TableReplay.chippos_x[strdraw_idx], TableReplay.chippos_y[strdraw_idx], anchor = 'nw', image=self.chips_3bb)
            else:
                self.vilchips_img = self.create_image(TableReplay.chippos_x[strdraw_idx], TableReplay.chippos_y[strdraw_idx], anchor = 'nw', image=self.chips_2p5bb)
        elif self.situation_index == 2:
            strdraw_idx = 4
            self.herochips_img =self.create_image(TableReplay.chippos_x[strdraw_idx], TableReplay.chippos_y[strdraw_idx], anchor = 'nw', image=self.chips_2p5bb)
            strdraw_idx = (vilpos_idx + 4 - heropos_idx) % 6
            self.vilchips_img = self.create_image(TableReplay.chippos_x[strdraw_idx], TableReplay.chippos_y[strdraw_idx], anchor = 'nw', image=self.chips_8bb)
        else:
            strdraw_idx = 4
            self.herochips_img = self.create_image(TableReplay.chippos_x[strdraw_idx], TableReplay.chippos_y[strdraw_idx], anchor = 'nw', image=self.chips_8bb)
            strdraw_idx = (vilpos_idx + 4 - heropos_idx) % 6
            self.vilchips_img = self.create_image(TableReplay.chippos_x[strdraw_idx], TableReplay.chippos_y[strdraw_idx], anchor = 'nw', image=self.chips_20bb) 
        
        self.itemconfigure(self.vilchips_img, state='hidden')
        self.itemconfigure(self.herochips_img, state='hidden')
        
        # draw hand
        self.hand1crd_img = self.create_text(351, 347, text='', anchor='e', font=("Consolas", 20, 'bold'), fill=TableReplay.suits[self.herocards[1]])
        self.hand2crd_img = self.create_text(402, 347, text='', anchor='e', font=("Consolas", 20, 'bold'), fill=TableReplay.suits[self.herocards[3]]) 
        self.hand1suit_img = self.create_image(337, 358, anchor='nw', image=self.blank)
        self.hand2suit_img = self.create_image(388, 358, anchor='nw', image=self.blank)
            
    def update(self):
        heropos_idx = TableReplay.pos_str.index(self.heropos)
        vilpos_idx = TableReplay.pos_str.index(self.vilpos)
        
        # update position labels
        for i in range(6):
            strdraw_idx = (heropos_idx + 2 + i) % 6
            self.itemconfig(self.poslabels[i], text=TableReplay.pos_str[strdraw_idx])
            
        # update sb and bb and btn marker
        self.delete(self.sb_img)
        self.delete(self.bb_img)
        self.delete(self.btn_img)
        strdraw_idx = (5 - heropos_idx) % 6
        self.sb_img = self.create_image(TableReplay.chippos_x[strdraw_idx], TableReplay.chippos_y[strdraw_idx], anchor = 'nw', image=self.chips_sb)
        strdraw_idx = (6 - heropos_idx) % 6
        self.bb_img = self.create_image(TableReplay.chippos_x[strdraw_idx], TableReplay.chippos_y[strdraw_idx], anchor = 'nw', image=self.chips_bb)
        strdraw_idx = (4 - heropos_idx) % 6
        self.btn_img = self.create_image(TableReplay.btn_x[strdraw_idx], TableReplay.btn_y[strdraw_idx], anchor = 'nw', image=self.bn_marker)
        
        # update raise and open chips, and delete overlapping images
        if self.vilchips_img:
            self.delete(self.vilchips_img)
        if self.herochips_img:
            self.delete(self.herochips_img)
            
        if self.situation_index == 0:
            pass
        
        elif self.situation_index == 1:
            strdraw_idx = (vilpos_idx + 4 - heropos_idx) % 6
            if self.vilpos in ['MP', 'EP']:
                if self.bet_size == '2.25bb':
                    self.vilchips_img = self.create_image(TableReplay.chippos_x[strdraw_idx], TableReplay.chippos_y[strdraw_idx], anchor = 'nw', image=self.chips_2p25bb)
                elif self.bet_size == '3bb':
                    self.vilchips_img = self.create_image(TableReplay.chippos_x[strdraw_idx], TableReplay.chippos_y[strdraw_idx], anchor = 'nw', image=self.chips_3bb)
            elif self.vilpos == 'SB':
                if self.bet_size == '3bb':
                    self.vilchips_img = self.create_image(TableReplay.chippos_x[strdraw_idx], TableReplay.chippos_y[strdraw_idx], anchor = 'nw', image=self.chips_3bb)
                elif self.bet_size == '3.5bb':
                    self.vilchips_img = self.create_image(TableReplay.chippos_x[strdraw_idx], TableReplay.chippos_y[strdraw_idx], anchor = 'nw', image=self.chips_3p5bb)
            else:
                if self.bet_size == '2.5bb':
                    self.vilchips_img = self.create_image(TableReplay.chippos_x[strdraw_idx], TableReplay.chippos_y[strdraw_idx], anchor = 'nw', image=self.chips_2p5bb)
                elif self.bet_size == '3bb':
                    self.vilchips_img = self.create_image(TableReplay.chippos_x[strdraw_idx], TableReplay.chippos_y[strdraw_idx], anchor = 'nw', image=self.chips_3bb)
            if vilpos_idx == 1:
                self.delete(self.sb_img)
                
        elif self.situation_index == 2:
            strdraw_idx = 4
            
            if self.heropos in ['MP', 'EP', 'CO']:
                self.herochips_img =self.create_image(TableReplay.chippos_x[strdraw_idx], TableReplay.chippos_y[strdraw_idx], anchor = 'nw', image=self.chips_2p25bb)
                strdraw_idx = (vilpos_idx + 4 - heropos_idx) % 6
                if self.vilpos == 'MP':
                    self.vilchips_img = self.create_image(TableReplay.chippos_x[strdraw_idx], TableReplay.chippos_y[strdraw_idx], anchor = 'nw', image=self.chips_7p5bb)
                elif self.vilpos in ['BN', 'CO']:
                    self.vilchips_img = self.create_image(TableReplay.chippos_x[strdraw_idx], TableReplay.chippos_y[strdraw_idx], anchor = 'nw', image=self.chips_8bb)
                elif self.vilpos == 'SB':
                    self.vilchips_img = self.create_image(TableReplay.chippos_x[strdraw_idx], TableReplay.chippos_y[strdraw_idx], anchor = 'nw', image=self.chips_11bb)
                else:
                    self.vilchips_img = self.create_image(TableReplay.chippos_x[strdraw_idx], TableReplay.chippos_y[strdraw_idx], anchor = 'nw', image=self.chips_12p5bb)
            elif self.heropos == 'SB':
                self.herochips_img =self.create_image(TableReplay.chippos_x[strdraw_idx], TableReplay.chippos_y[strdraw_idx], anchor = 'nw', image=self.chips_3bb)
                strdraw_idx = (vilpos_idx + 4 - heropos_idx) % 6
                self.vilchips_img = self.create_image(TableReplay.chippos_x[strdraw_idx], TableReplay.chippos_y[strdraw_idx], anchor = 'nw', image=self.chips_9bb)
            else:
                self.herochips_img =self.create_image(TableReplay.chippos_x[strdraw_idx], TableReplay.chippos_y[strdraw_idx], anchor = 'nw', image=self.chips_2p5bb)
                strdraw_idx = (vilpos_idx + 4 - heropos_idx) % 6
                if self.vilpos == 'SB':
                    self.vilchips_img = self.create_image(TableReplay.chippos_x[strdraw_idx], TableReplay.chippos_y[strdraw_idx], anchor = 'nw', image=self.chips_11bb)
                else:
                    self.vilchips_img = self.create_image(TableReplay.chippos_x[strdraw_idx], TableReplay.chippos_y[strdraw_idx], anchor = 'nw', image=self.chips_13p5bb)

            if heropos_idx == 1:
                self.delete(self.sb_img)
            if vilpos_idx == 1:
                self.delete(self.sb_img)
            if vilpos_idx == 2:
                self.delete(self.bb_img)
            
        else:
            strdraw_idx = 4
            if self.heropos == 'SB':
                self.herochips_img = self.create_image(TableReplay.chippos_x[strdraw_idx], TableReplay.chippos_y[strdraw_idx], anchor = 'nw', image=self.chips_11bb)
            elif self.heropos == 'MP':
                self.herochips_img = self.create_image(TableReplay.chippos_x[strdraw_idx], TableReplay.chippos_y[strdraw_idx], anchor = 'nw', image=self.chips_7p5bb)
            elif self.heropos == 'BB':
                if self.vilpos == 'SB':
                    self.herochips_img = self.create_image(TableReplay.chippos_x[strdraw_idx], TableReplay.chippos_y[strdraw_idx], anchor = 'nw', image=self.chips_9bb)
                elif self.vilpos == 'BN':
                    self.herochips_img = self.create_image(TableReplay.chippos_x[strdraw_idx], TableReplay.chippos_y[strdraw_idx], anchor = 'nw', image=self.chips_13p5bb)
                else:
                    self.herochips_img = self.create_image(TableReplay.chippos_x[strdraw_idx], TableReplay.chippos_y[strdraw_idx], anchor = 'nw', image=self.chips_12p5bb)
            else:
                self.herochips_img = self.create_image(TableReplay.chippos_x[strdraw_idx], TableReplay.chippos_y[strdraw_idx], anchor = 'nw', image=self.chips_8bb)

            strdraw_idx = (vilpos_idx + 4 - heropos_idx) % 6

            if self.heropos == 'SB':
                self.vilchips_img = self.create_image(TableReplay.chippos_x[strdraw_idx], TableReplay.chippos_y[strdraw_idx], anchor = 'nw', image=self.chips_23bb)
            elif self.heropos == 'BB':
                self.vilchips_img = self.create_image(TableReplay.chippos_x[strdraw_idx], TableReplay.chippos_y[strdraw_idx], anchor = 'nw', image=self.chips_26p5bb)
            else:
                self.vilchips_img = self.create_image(TableReplay.chippos_x[strdraw_idx], TableReplay.chippos_y[strdraw_idx], anchor = 'nw', image=self.chips_20bb)

            if heropos_idx == 1:
                self.delete(self.sb_img)
            if heropos_idx == 2:
                self.delete(self.bb_img)  
            if vilpos_idx == 1:
                self.delete(self.sb_img)
            
        # update dealt hand
        if self.hand1crd_img:
            self.delete(self.hand1crd_img)
            self.delete(self.hand2crd_img)
            self.delete(self.hand1suit_img)
            self.delete(self.hand2suit_img)
            
            self.hand1crd_img = self.create_text(351, 347, text=self.herocards[0], anchor='e', font=("Consolas", 20, 'bold'), fill=TableReplay.suits[self.herocards[1]])
            self.hand2crd_img = self.create_text(402, 347, text=self.herocards[2], anchor='e', font=("Consolas", 20, 'bold'), fill=TableReplay.suits[self.herocards[3]]) 
            
            if self.herocards[1] == 'h':
                self.hand1suit_img = self.create_image(337, 358, anchor='nw', image=self.suit_h)
            elif self.herocards[1] == 'c':
                self.hand1suit_img = self.create_image(337, 358, anchor='nw', image=self.suit_c)
            elif self.herocards[1] == 'd':
                self.hand1suit_img = self.create_image(337, 358, anchor='nw', image=self.suit_d)
            elif self.herocards[1] == 's':
                self.hand1suit_img = self.create_image(337, 358, anchor='nw', image=self.suit_s)
                
            if self.herocards[3] == 'h':
                self.hand2suit_img = self.create_image(388, 358, anchor='nw', image=self.suit_h)
            if self.herocards[3] == 'c':
                self.hand2suit_img = self.create_image(388, 358, anchor='nw', image=self.suit_c)
            if self.herocards[3] == 'd':
                self.hand2suit_img = self.create_image(388, 358, anchor='nw', image=self.suit_d)
            if self.herocards[3] == 's':
                self.hand2suit_img = self.create_image(388, 358, anchor='nw', image=self.suit_s)
        