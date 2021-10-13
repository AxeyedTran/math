import os, math, time, sys
d = '\033[1;91m'
xl = '\033[1;92m'
v = '\033[1;93m'
xb = '\033[1;96m'
t = '\033[1;97m'
def write(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.001)
def load():
	kha = ['.   ','..  ','... ']
	for o in kha:
		print("\r\033[1;97m[\033[1;96m*\033[1;97m] \033[1;92mLoading \033[1;97m"+o),;sys.stdout.flush();time.sleep(1)
f = "\033[1;97m------------------------------------------------------------"
banner = """
\033[1;97m╔═\033[1;97m════════\033[1;97m╗  ╔════════════════════════════════════════════════════╗
\033[1;97m║ \033[1;96m██╗  ██╗\033[1;97m║  ║ [\033[1;92m*\033[1;97m] \033[1;96mTác Giả:  Trần Bảo Kha  (Axeyed Kha)\033[1;97m           ║   
\033[1;97m║ \033[1;95m██║ ██╔╝\033[1;97m║  ║ [\033[1;92m*\033[1;97m] \033[1;92mTool Tính Điểm Trung Bình  \033[1;97m                    ║
\033[1;97m║ \033[1;92m█████╔╝ \033[1;97m║  ║ [\033[1;92m*\033[1;97m] \033[1;95mFacebook: Axeyed kha\033[1;97m                           ║ 
\033[1;97m║ \033[1;93m██╔═██╗ \033[1;97m║  ║ [\033[1;92m*\033[1;97m] \033[1;93mGmail: axeyedkha191@gmail.com\033[1;97m                  ║
\033[1;97m║ \033[1;94m██║  ██╗\033[1;97m║  ║ [\033[1;92m*\033[1;97m] \033[1;92mVersion: 2.2  #DEV: Axeyed Kha\033[1;97m                 ║
\033[1;97m║ \033[1;97m╚═╝  ╚═╝\033[1;97m║  ║ [\033[1;92m*\033[1;97m] \033[1;94mTP: Thừa Thiên Huế\033[1;97m                             ║
\033[1;97m╚═\033[1;97m════════\033[1;97m╝  ╚════════════════════════════════════════════════════╝
"""
def main():
  os.system('clear')
  write(banner)
  write(xl+'Chào mừng bạn đến với hệ thống tính điểm trung bình.')
  write(xb+'DEV: Tran Bao Kha')
  write(f)
  load()
  menu()
def yn():
  write(f)
  cnbn = input('Bạn có muốn quay về lại menu không? [y/n] :')
  if cnbn == 'y' or cnbn == 'Y':
    menu()
  elif cnbn == 'n' or cnbn == 'N':
    print('\033[1;96m Cám ơn bạn đã sử dụng công cụ của tôi')
    os.sys.exit()
  else:
    print(d+'[!] Nhập sai')
    os.sys.exit()
def menu():
  os.system('clear')
  write(banner)
  write(f)
  write(t+'['+xl+'1'+t+'] Tính điểm trung bình 2 môn')
  write(t+'['+xl+'2'+t+'] Tính điểm trung bình 3 môn')
  write(t+'['+xl+'3'+t+'] Tính điểm trung bình 4 môn')
  write(t+'['+xl+'4'+t+'] Tính điểm trung bình 5 môn')
  write(t+'['+xl+'5'+t+'] Tính điểm trung bình 6 môn')
  write(t+'['+xl+'6'+t+'] Tính điểm trung bình 7 môn')
  write(t+'['+xl+'7'+t+'] Tính điểm trung bình 8 môn')
  write(t+'['+xl+'8'+t+'] Tính điểm trung bình 9 môn')
  write(t+'['+xl+'9'+t+'] Tính điểm trung bình 10 môn')
  write(t+'['+xl+'10'+t+'] Tính điểm trung bình 11 môn')
  write(t+'['+xl+'11'+t+'] Tính điểm trung bình 12 môn')
  write(t+'['+xl+'12'+t+'] Tính điểm trung bình 13 môn')
  write(f)
  q = input(t+'[?] Nhập lựa chọn của bạn: '+xl)
  if q == '1' or q == '01':
    k2()
  elif q == '2' or q == '02':
    k3()
  elif q == '3' or q == '03':
    k4()
  elif q == '4' or q == '04':
    k5()
  elif q == '5' or q == '05':
    k6()
  elif q == '6' or q == '06':
    k7()
  elif q == '7' or q == '07':
    k8()
  elif q == '8' or q == '08':
    k9() 
  elif q == '9' or q == '09':
    k10()
  elif q == '10' or q == '10':
    k11()
  elif q == '11' or q == '11':
    k12()
  elif q == '12' or q == '12':
    k13()
  else:
        print(d+'[!] Nhập Sai')
        os.sys.exit()
def k2():
  os.system('clear')
  write(banner)
  print(f)
  k = float(input('Nhập Điểm môn thứ 1 : '))
  write(f)
  kk = float(input('Nhập điểm môn thứ 2 : '))
  write(f)
  write(f)
  re = (k+kk)/2
  load()
  write('Điểm trung bình là %.2f:'%re)
  write(f)
  if (re < 5):
        print("Học lực yếu")
  elif(re >=5 and re < 7):
        print("Học lực trung bình")
  elif(re >=7 and re < 9):
        print("Học lực khá")
  elif(re >=9):
        print("Học lực giỏi")
  yn()
def k3():
  os.system('clear')
  write(banner)
  print(f)
  k = float(input('Nhập Điểm môn thứ 1 : '))
  write(f)
  kk = float(input('Nhập điểm môn thứ 2 : '))
  write(f)
  kkk = float(input('Nhập điểm môn thứ 3 :'))
  write(f)
  re = (k+kk+kkk)/3
  load()
  write('Điểm trung bình là %.2f:'%re)
  write(f)
  if (re < 5):
        print("Học lực yếu")
  elif(re >=5 and re < 7):
        print("Học lực trung bình")
  elif(re >=7 and re < 9):
        print("Học lực khá")
  elif(re >=9):
        print("Học lực giỏi")
  yn()
def k4():
  os.system('clear')
  write(banner)
  print(f)
  k = float(input('Nhập Điểm môn thứ 1 : '))
  write(f)
  kk = float(input('Nhập điểm môn thứ 2 : '))
  write(f)
  kkk = float(input('Nhập điểm môn thứ 3 :'))
  write(f)
  kkkk = float(input('Nhập điểm môn thứ 4 :'))
  write(f)
  re = (k+kk+kkk+kkkk)/4
  load()
  write('Điểm trung bình là %.2f:'%re)
  write(f)
  if (re < 5):
        print("Học lực yếu")
  elif(re >=5 and re < 7):
        print("Học lực trung bình")
  elif(re >=7 and re < 9):
        print("Học lực khá")
  elif(re >=9):
        print("Học lực giỏi")
  yn()
def k5():
  os.system('clear')
  write(banner)
  print(f)
  k = float(input('Nhập Điểm môn thứ 1 : '))
  write(f)
  kk = float(input('Nhập điểm môn thứ 2 : '))
  write(f)
  kkk = float(input('Nhập điểm môn thứ 3 :'))
  write(f)
  kkkk = float(input('Nhập điểm môn thứ 4 :'))
  write(f)
  kkkkk = float(input('Nhập điểm môn thứ 5 :'))
  write(f)
  re = (k+kk+kkk+kkkk+kkkkk)/5
  load()
  write('Điểm trung bình là %.2f:'%re)
  write(f)
  if (re < 5):
        print("Học lực yếu")
  elif(re >=5 and re < 7):
        print("Học lực trung bình")
  elif(re >=7 and re < 9):
        print("Học lực khá")
  elif(re >=9):
        print("Học lực giỏi")
  yn()
def k6():
  os.system('clear')
  write(banner)
  print(f)
  k = float(input('Nhập Điểm môn thứ 1 : '))
  write(f)
  kk = float(input('Nhập điểm môn thứ 2 : '))
  write(f)
  kkk = float(input('Nhập điểm môn thứ 3 :'))
  write(f)
  kkkk = float(input('Nhập điểm môn thứ 4 :'))
  write(f)
  kkkkk = float(input('Nhập điểm môn thứ 5 :'))
  write(f)
  kkkkkk = float(input('Nhập điểm môn thứ 6 :'))
  write(f)
  re = (k+kk+kkk+kkkk+kkkkk+kkkkkk)/6
  load()
  write('Điểm trung bình là %.2f:'%re)
  write(f)
  if (re < 5):
        print("Học lực yếu")
  elif(re >=5 and re < 7):
        print("Học lực trung bình")
  elif(re >=7 and re < 9):
        print("Học lực khá")
  elif(re >=9):
        print("Học lực giỏi")
  yn()
def k7():
  os.system('clear')
  write(banner)
  print(f)
  k = float(input('Nhập Điểm môn thứ 1 : '))
  write(f)
  kk = float(input('Nhập điểm môn thứ 2 : '))
  write(f)
  kkk = float(input('Nhập điểm môn thứ 3 :'))
  write(f)
  kkkk = float(input('Nhập điểm môn thứ 4 :'))
  write(f)
  kkkkk = float(input('Nhập điểm môn thứ 5 :'))
  write(f)
  kkkkkk = float(input('Nhập điểm môn thứ 6 :'))
  write(f)
  kkkkkkk = float(input('Nhập điểm môn thứ 7 :'))
  write(f)
  re = (k+kk+kkk+kkkk+kkkkk+kkkkkk+kkkkkkk)/7
  load()
  write('Điểm trung bình là %.2f:'%re)
  write(f)
  if (re < 5):
        print("Học lực yếu")
  elif(re >=5 and re < 7):
        print("Học lực trung bình")
  elif(re >=7 and re < 9):
        print("Học lực khá")
  elif(re >=9):
        print("Học lực giỏi")
  yn()
def k8():
  os.system('clear')
  write(banner)
  print(f)
  k = float(input('Nhập Điểm môn thứ 1 : '))
  write(f)
  kk = float(input('Nhập điểm môn thứ 2 : '))
  write(f)
  kkk = float(input('Nhập điểm môn thứ 3 :'))
  write(f)
  kkkk = float(input('Nhập điểm môn thứ 4 :'))
  write(f)
  kkkkk = float(input('Nhập điểm môn thứ 5 :'))
  write(f)
  kkkkkk = float(input('Nhập điểm môn thứ 6 :'))
  write(f)
  kkkkkkk = float(input('Nhập điểm môn thứ 7 :'))
  write(f)
  kkkkkkkk = float(input('Nhập điểm môn thứ 8 :'))
  write(f)
  re = (k+kk+kkk+kkkk+kkkkk+kkkkkk+kkkkkkk+kkkkkkkk)/8
  load()
  write('Điểm trung bình là %.2f:'%re)
  write(f)
  if (re < 5):
        print("Học lực yếu")
  elif(re >=5 and re < 7):
        print("Học lực trung bình")
  elif(re >=7 and re < 9):
        print("Học lực khá")
  elif(re >=9):
        print("Học lực giỏi")
  yn()
def k9():
  os.system('clear')
  write(banner)
  print(f)
  k = float(input('Nhập Điểm môn thứ 1 : '))
  write(f)
  kk = float(input('Nhập điểm môn thứ 2 : '))
  write(f)
  kkk = float(input('Nhập điểm môn thứ 3 :'))
  write(f)
  kkkk = float(input('Nhập điểm môn thứ 4 :'))
  write(f)
  kkkkk = float(input('Nhập điểm môn thứ 5 :'))
  write(f)
  kkkkkk = float(input('Nhập điểm môn thứ 6 :'))
  write(f)
  kkkkkkk = float(input('Nhập điểm môn thứ 7 :'))
  write(f)
  kkkkkkkk = float(input('Nhập điểm môn thứ 8 :'))
  write(f)
  kkkkkkkkk = float(input('Nhập điểm môn thứ 9 :'))
  write(f)
  re = (k+kk+kkk+kkkk+kkkkk+kkkkkk+kkkkkkk+kkkkkkkk+kkkkkkkkk)/9
  load()
  write('Điểm trung bình là %.2f:'%re)
  write(f)
  if (re < 5):
        print("Học lực yếu")
  elif(re >=5 and re < 7):
        print("Học lực trung bình")
  elif(re >=7 and re < 9):
        print("Học lực khá")
  elif(re >=9):
        print("Học lực giỏi")
  yn()
def k10():
  os.system('clear')
  write(banner)
  print(f)
  k = float(input('Nhập Điểm môn thứ 1 : '))
  write(f)
  kk = float(input('Nhập điểm môn thứ 2 : '))
  write(f)
  kkk = float(input('Nhập điểm môn thứ 3 :'))
  write(f)
  kkkk = float(input('Nhập điểm môn thứ 4 :'))
  write(f)
  kkkkk = float(input('Nhập điểm môn thứ 5 :'))
  write(f)
  kkkkkk = float(input('Nhập điểm môn thứ 6 :'))
  write(f)
  kkkkkkk = float(input('Nhập điểm môn thứ 7 :'))
  write(f)
  kkkkkkkk = float(input('Nhập điểm môn thứ 8 :'))
  write(f)
  kkkkkkkkk = float(input('Nhập điểm môn thứ 9 :'))
  write(f)
  kkkkkkkkkk = float(input('Nhập điểm môn thứ 10 :'))
  write(f)
  re = (k+kk+kkk+kkkk+kkkkk+kkkkkk+kkkkkkk+kkkkkkkk+kkkkkkkkk+kkkkkkkkkk)/10
  load()
  write('Điểm trung bình là %.2f:'%re)
  write(f)
  if (re < 5):
        print("Học lực yếu")
  elif(re >=5 and re < 7):
        print("Học lực trung bình")
  elif(re >=7 and re < 9):
        print("Học lực khá")
  elif(re >=9):
        print("Học lực giỏi")
  yn()
def k11():
  os.system('clear')
  write(banner)
  print(f)
  k = float(input('Nhập Điểm môn thứ 1 : '))
  write(f)
  kk = float(input('Nhập điểm môn thứ 2 : '))
  write(f)
  kkk = float(input('Nhập điểm môn thứ 3 :'))
  write(f)
  kkkk = float(input('Nhập điểm môn thứ 4 :'))
  write(f)
  kkkkk = float(input('Nhập điểm môn thứ 5 :'))
  write(f)
  kkkkkk = float(input('Nhập điểm môn thứ 6 :'))
  write(f)
  kkkkkkk = float(input('Nhập điểm môn thứ 7 :'))
  write(f)
  kkkkkkkk = float(input('Nhập điểm môn thứ 8 :'))
  write(f)
  kkkkkkkkk = float(input('Nhập điểm môn thứ 9 :'))
  write(f)
  kkkkkkkkkk = float(input('Nhập điểm môn thứ 10 :'))
  write(f)
  kkkkkkkkkkk = float(input('Nhập điểm môn thứ 11 :'))
  write(f)
  re = (k+kk+kkk+kkkk+kkkkk+kkkkkk+kkkkkkk+kkkkkkkk+kkkkkkkkk+kkkkkkkkkk+kkkkkkkkkkk)/11
  load()
  write('Điểm trung bình là %.2f:'%re)
  write(f)
  if (re < 5):
        print("Học lực yếu")
  elif(re >=5 and re < 7):
        print("Học lực trung bình")
  elif(re >=7 and re < 9):
        print("Học lực khá")
  elif(re >=9):
        print("Học lực giỏi")
  yn()
def k12():
  os.system('clear')
  write(banner)
  print(f)
  k = float(input('Nhập Điểm môn thứ 1 : '))
  write(f)
  kk = float(input('Nhập điểm môn thứ 2 : '))
  write(f)
  kkk = float(input('Nhập điểm môn thứ 3 :'))
  write(f)
  kkkk = float(input('Nhập điểm môn thứ 4 :'))
  write(f)
  kkkkk = float(input('Nhập điểm môn thứ 5 :'))
  write(f)
  kkkkkk = float(input('Nhập điểm môn thứ 6 :'))
  write(f)
  kkkkkkk = float(input('Nhập điểm môn thứ 7 :'))
  write(f)
  kkkkkkkk = float(input('Nhập điểm môn thứ 8 :'))
  write(f)
  kkkkkkkkk = float(input('Nhập điểm môn thứ 9 :'))
  write(f)
  kkkkkkkkkk = float(input('Nhập điểm môn thứ 10 :'))
  write(f)
  kkkkkkkkkkk = float(input('Nhập điểm môn thứ 11 :'))
  write(f)
  kkkkkkkkkkkk = float(input('Nhập điểm môn thứ 12 :'))
  write(f)
  re = (k+kk+kkk+kkkk+kkkkk+kkkkkk+kkkkkkk+kkkkkkkk+kkkkkkkkk+kkkkkkkkkk+kkkkkkkkkkk+kkkkkkkkkkkk)/12
  load()
  write('Điểm trung bình là %.2f:'%re)
  write(f)
  if (re < 5):
        print("Học lực yếu")
  elif(re >=5 and re < 7):
        print("Học lực trung bình")
  elif(re >=7 and re < 9):
        print("Học lực khá")
  elif(re >=9):
        print("Học lực giỏi")
  yn()
def k13():
  os.system('clear')
  write(banner)
  print(f)
  k = float(input('Nhập Điểm môn thứ 1 : '))
  write(f)
  kk = float(input('Nhập điểm môn thứ 2 : '))
  write(f)
  kkk = float(input('Nhập điểm môn thứ 3 :'))
  write(f)
  kkkk = float(input('Nhập điểm môn thứ 4 :'))
  write(f)
  kkkkk = float(input('Nhập điểm môn thứ 5 :'))
  write(f)
  kkkkkk = float(input('Nhập điểm môn thứ 6 :'))
  write(f)
  kkkkkkk = float(input('Nhập điểm môn thứ 7 :'))
  write(f)
  kkkkkkkk = float(input('Nhập điểm môn thứ 8 :'))
  write(f)
  kkkkkkkkk = float(input('Nhập điểm môn thứ 9 :'))
  write(f)
  kkkkkkkkkk = float(input('Nhập điểm môn thứ 10 :'))
  write(f)
  kkkkkkkkkkk = float(input('Nhập điểm môn thứ 11 :'))
  write(f)
  kkkkkkkkkkkk = float(input('Nhập điểm môn thứ 12 :'))
  write(f)
  kkkkkkkkkkkkk = float(input('Nhập điểm môn thứ 13 :'))
  write(f)
  re = (k+kk+kkk+kkkk+kkkkk+kkkkkk+kkkkkkk+kkkkkkkk+kkkkkkkkk+kkkkkkkkkk+kkkkkkkkkkk+kkkkkkkkkkkk+kkkkkkkkkkkkk)/13
  load()
  write('Điểm trung bình là %.2f:'%re)
  write(f)
  if (re < 5):
        print("Học lực yếu")
  elif(re >=5 and re < 7):
        print("Học lực trung bình")
  elif(re >=7 and re < 9):
        print("Học lực khá")
  elif(re >=9):
        print("Học lực giỏi")
  yn()
#=====RUN TOOL=====#
main()