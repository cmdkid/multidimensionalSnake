# Multidimensional snake  
## run:
In IDE set breakpoint on "field.tic()" in main.py  
Use debugger next step hotkey to move.  
To rotate: run command `field.control(dimension_id: int, rotate: int)`  
where **dimension_id** is index of dimension, where rotate to  
and **rotate** is 1 or -1 for counterclockwise or clockwise rotation  
  
  
# simple run with bot control:  
You can select one of bot control functions, by uncommenting `bot_*` function in main.py.  
I do not recommend to use multiple bots simultaneously, this will probably kill the snake by ticking head into it own body.  
  
## config.py:  
To change dimension size, just write each dimension size in conf_data['field'] list  
  