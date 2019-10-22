import maya.cmds as cmds
import os

title='Miyamo Texture Manager'
ver='1.0.0'

def scan():
    file=cmds.ls(tex=True)
    cmds.textScrollList('tsl', e=True, ra=True)
    for i in file:
        s=''
        if os.path.exists(cmds.getAttr(i+'.fileTextureName'))==False:
            s+=' ! | '
        cmds.textScrollList('tsl', e=True, a=s+cmds.getAttr(i+'.fileTextureName'))

win = cmds.window( t=title, widthHeight=(600,400) )
form = cmds.formLayout( nd=100 )

bAN = cmds.button(l='Analyze Textures', height=26, c='scan()')
txTL = cmds.text('txTL', l='Texture(s) List')
tsl = cmds.textScrollList('tsl', h=150)
txI = cmds.text('txI', l='Texture Information')

b1 = cmds.button( label='Command 1', height=30, command='' )
b2 = cmds.button( label='Set Path', height=30, command='' )
b3 = cmds.button( label='Close', height=30, command='cmds.deleteUI(win, wnd = True)' )

cmds.formLayout(
            form, edit=True, \
            #フォームの境界にボタンのどのエッジを固定するかの指定。オフセット値を5としている。
            attachForm = (  [bAN, 'top', 5], \
                            [txTL, 'left', 5], \
                            [tsl, 'left', 5], [tsl, 'right', 5], \
                            [txI, 'left', 5], \
                            [ b1, 'left', 5 ], \
                            [ b1, 'bottom', 5 ], \
                            [ b2, 'bottom', 5 ], \
                            [ b3, 'bottom', 5 ], \
                            [ b3, 'right', 5 ]), \
            #ボタンをフォームのどの位置に固定するかの指定。b1の右辺を33%の位置に、b3の左辺を67%の位置に。
            attachPosition = (  [bAN, 'left', 5, 0], [bAN, 'right', 5, 100], \
                                [b1, 'right' , 0, 33], \
                                [b3, 'left' , 0, 67] ), \
            #真ん中のボタンb2が左右のボタンの隣接する辺に固定ための設定。
            attachControl = (   [txTL, 'top', 5, bAN], \
                                [tsl, 'top', 5, txTL], \
                                [txI, 'top', 5, tsl], \
                                [ b2, 'left', 4,  b1 ], \
                                [ b2, 'right', 4, b3 ] ),\
            #すべてのボタンの上辺は固定しない。
            attachNone = ( [ b1, 'top' ], [ b2, 'top' ], [ b3, 'top' ] )
            )

cmds.showWindow()
