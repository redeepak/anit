import pyqrcode as df

qr = df.create('houston_system_private_ltd')

qr.png('hello.png', scale=7)

qr.svg('s_v_g.svg')

qr.eps("e_p_s.eps")




