import math                         # mathモジュールをインポート
import cmath                        # cmathモジュールをインポート(複素数計算の対応のため)
import time                         # timeモジュールをインポート
import random                       # randomモジュールをインポート
import fractions                    # fractionsモジュールをインポート

# デモ関数定義 引数で表示速度変更 初期値0.1
def demo(speed = 0.1):
    for i in "This is Simple calculator.\n":
        print(i,end="",flush=True)
        time.sleep(speed)

    for i in "This app was made by K.Yuya on July 22th 2020.\n":
        print(i,end="",flush=True)
        time.sleep(speed)

    for i in "You can use variables yourselves.\n":
        print(i,end="",flush=True)
        time.sleep(speed)

    for i in "Enjoy your Calculation lives.\n":
        print(i,end="",flush=True)
        time.sleep(speed)

    return "Thank you for using this app!!"


pi = math.pi                        # 円周率をpiに代入
tau = math.tau                      # τ(タウ)をtauに代入(円周率の2倍の値)
e = math.e                          # 自然対数の底をeに代入
inf = float("inf")                  # 無限大をinfに代入
nan = float("nan")                  # 存在しない数、非数(削除予定)
i = 1j                              # 虚数単位をiに代入(Pythonでは複素数をa+bjと表す。)

# 分数の定義 (p/q)
def fraction(p, q = "none"):
    if q == 0:
        return float("nan")
    elif type(p) is complex or type(q) is complex:
        return p/q
    elif q == "none":
        return fractions.Fraction(p).limit_denominator()
    else:
        return fractions.Fraction(p, q).limit_denominator()
# 分数の定義(省略形) (p/q)
def fr(p, q = "none"):
    return fraction(p, q)

# 平方根の定義
def sqrt(num):
    if type(num) is complex or num < 0:               # numが複素数または0より小さいときにcmath使用
        return cmath.sqrt(num)
    elif math.sqrt(num)%1 == 0 and type(num) is int:
        return int(math.sqrt(num))
    else:
        return math.sqrt(num)

# 度数法を弧度法に変える関数の定義
def rad(num):
    return (num/180)*math.pi

# 三角関数 正弦(sin)の定義
def sin(num):
    if num.imag == 0:                                   #numが実数か複素数で判定
        if num.real%pi == 0:
            return 0
        elif (num.real-(math.pi/2))%(math.pi*2) == 0:
            return 1
        elif (num.real+(math.pi/2))%(math.pi*2) == 0:
            return -1
        else:
            return math.sin(num.real)
    else:                                               # numが複素数のときにcmath使用
        return cmath.sin(num)

# 三角関数 余弦(cos)の定義
def cos(num):
    if num.imag == 0:                                   #numが実数か複素数で判定
        if num.real%math.pi == 0:
            if (num.real%(math.pi*2)) == 0:
                return 1
            else:
                return -1
        elif (num.real+(math.pi/2))%math.pi == 0:
            return 0
        else:
            return math.cos(num.real)
    else:                                               # numが複素数のときにcmath使用
        return cmath.cos(num)

# 三角関数 正接(tan)の定義
def tan(num):
    if num.imag == 0:                                   #numが実数か複素数で判定
        if ((num.real+(math.pi/2))%math.pi) == 0:
            return float("nan")
        elif num.real%pi == 0:
            return 0
        else:
            return math.tan(num.real)
    else:                                               # numが複素数のときにcmath使用
        return cmath.tan(num)

# 逆三角関数 asinの定義
def asin(num):
    if type(num) is complex or num < -1 or num > 1:     # numが複素数またはnum<-1またはnum>1のときにcmath使用
        return cmath.asin(num)
    return math.asin(num)

# 逆三角関数 acosの定義
def acos(num):
    if type(num) is complex or num < -1 or num > 1:     # numが複素数またはnum<-1またはnum>1のときにcmath使用
        return cmath.acos(num)
    return math.acos(num)

# 逆三角関数 atanの定義
def atan(num):
    if type(num) is complex:                            # numが複素数のときにcmath使用
        return cmath.atan(num)
    return math.atan(num)

# 双曲線関数 sinhの定義
def sinh(num):
    if type(num) is complex:                            # numが複素数のときにcmath使用
        return cmath.sinh(num)
    return math.sinh(num)

# 双曲線関数 coshの定義
def cosh(num):
    if type(num) is complex:                            # numが複素数のときにcmath使用
        return cmath.cosh(num)
    return math.cosh(num)

# 双曲線関数 tanhの定義
def tanh(num):
    if type(num) is complex:                            # numが複素数のときにcmath使用
        return cmath.tanh(num)
    return math.tanh(num)

# 逆双曲線関数 asinhの定義
def asinh(num):
    if type(num) is complex:                            # numが複素数のときにcmath使用
        return cmath.asinh(num)
    return math.asinh(num)

# 逆双曲線関数 acoshの定義
def acosh(num):
    if type(num) is complex or num < 1:                 # numが複素数またはnum<1のときにcmath使用
        return cmath.acosh(num)
    return math.acosh(num)


# 逆双曲線関数 atanhの定義
def atanh(num):
    if num == 1:                                        # numが1のとき無限大を返す
        return float("inf")
    elif num == -1:
        return -float("inf")                            # numが-1のとき負の無限大を返す
    elif type(num) is complex or num < -1 or num > 1:   # numが複素数またはnum<-1またはnum>1のときにcmath使用
        return cmath.atanh(num)
    return math.atanh(num)

# 常用対数関数の定義
def log10(num):
    if num == 0:                                        # numが0のとき負の無限大を返す
        return -float("inf")
    if type(num) is complex or num < 0:
        return cmath.log10(num)
    return math.log10(num)

# 底が2の対数関数の定義
def log2(num):
    if num == 0:                                        # numが0のとき負の無限大を返す
        return -float("inf")
    if type(num) is complex or num < 0:
        return cmath.log(num, 2)
    return math.log2(num)

# 対数関数 pは真数 qは底 qの指定がないときは常用対数関数 定義
def log(p, q = 10):
    if p == 0:                                                      # 真数pが0のとき負の無限大を返す
        return -float("inf")
    if type(p) is complex or type(q) is complex or p < 0 or q < 0:  # numが複素数のときにcmath使用
        return cmath.log(p, q)
    return math.log(p, q)

# 自然対数の底の対数関数定の義
def ln(num):
    if num == 0:                                        # numが0のとき負の無限大を返す
        return -float("inf")
    if type(num) is complex or num < 0:
        return cmath.log(num)                           # numが複素数のときにcmath使用
    return math.log(num)

# 指数関数 (ネイピア数) の定義(cos()とsin()に依存)
def exp(num):
    if type(num) is complex and num.imag != 0:          # numが複素数のときにオイラーの公式を使用
        if num.imag%math.pi == 0:
            return math.exp(num.real)*cos(num.imag)
        return math.exp(num.real)*(cos(num.imag)+sin(num.imag)*1j)
    return math.exp(num.real)

# 階乗の定義
def fact(num):
    if num < 0 and num%1 == 0:
        return float("nan")
    if type(num) is float or num < 0:                   # numが少数または負の数の場合ガンマ関数を使用
        return math.gamma(num + 1)
    return math.factorial(num)

# ガンマ関数の定義
def gamma(num):
    if num <= 0 and num%1 == 0:
        return float("nan")
    return math.gamma(num)

# ガンマ関数に自然対数をとったものの定義
def lgamma(num):
    if num <= 0 and num%1 == 0:
        return float("nan")
    return math.lgamma(num)

# 複素数における偏角の定義
def arg(num):
    return cmath.phase(num)

# 複素数における極形式から直交形式の変換の定義 (exp()に依存,オイラーの公式使用(z=re^iθ))
def rect(r, phi):
    return r*exp(phi*1j)

# 最大公約数の定義
def gcd(a, b):
    if type(a) is complex or type(b) is complex:
        return float("nan")
    if a%1 != 0 or b%1 != 0:
        return float("nan")
    return math.gcd(a, b)

# 最小公倍数の定義
def lcm(a, b):
    if type(a) is complex or type(b) is complex:
        return float("nan")
    if a%1 != 0 or b%1 != 0 or a <= 0 or b <= 0:
        return float("nan")
    gcf = math.gcd(a, b)
    return int(a*b/gcf)

# 乱数(0≦x<1)の定義
def rand():
    return random.random()

# z=a+biとする時(0≦a<1,0≦b<1)を満たす複素数の乱数(絶対値が1以下の確率はπ/4)
def crand():
    return complex(random.random(), random.random())

# 乱数(p≦x≦q, int型)の定義
def randint(p, q):
    if type(p) is complex or type(q) is complex:
        return float("nan")
    if p%1 != 0 or q%1 != 0:
        return float("nan")
    if p > q:
        p, q = q, p
    return random.randint(p, q)

# 乱数(p≦x≦q, float型)の定義
def uniform(p, q):
    if type(p) is complex or type(q) is complex:
        return float("nan")
    if p > q:
        p, q = q, p
    return random.uniform(p, q)

# 繰り返し計算の定義
def forrange(start, end, step = 1):
    if type(start) is complex or type(end) is complex or type(step) is complex or type(step) is float:
        exit()

    if start > end and step > 0:
        step *= -1

    if (end-start)//step >= 10000:
        print("Warning: Potential crash")
        inputed = input("Do you want to continue?(y/n):")
        if inputed == "y" or inputed == "Y":
            print("Continue the calculation.")
        else:
            return "killed"

    Formula = input("Please type your Formula(variable:x):")
    Formula = Formula.replace("^", "**")
    ans = {}

    for x in range(start,end+1,step):
        result = eval(Formula)
        if type(result) is complex:
            result = round(result.real, 12) + round(result.imag, 12)*1j
        elif type(result) is float:
            result = round(result, 12)
        ans[x] = result
    return ans

# 決定的素数判定
def pnj(num):
    if type(num) is complex:
        return False
    if num == 2:
        return True
    if num%2 == 0 or num <= 1 or num%1 != 0:
        return False

    range_to_examine = int(math.sqrt(num))+1

    if range_to_examine%2 == 0:
        range_to_examine += 1
    for i in range(3,range_to_examine,2):
        if num%i == 0:
            return False
    return True

# 確率的素数判定(ミラーラビン素数判定法) 検出精度:99.99999999996793%
def mpnj(num, k = 100):
    if type(num) is complex:
        return False
    if num == 2:
        return True
    if num & 1 == 0 or num%2 == 0 or num <= 1 or num%1 != 0:
        return False

    d = (num - 1) >> 1
    while d & 1 == 0:
        d >>= 1

    for _ in range(k):
        a = random.randint(1, num - 1)
        t = d
        y = pow(a, t, num)

        while t != num - 1 and y != 1 and y != num - 1:
            y = (y * y) % num
            t <<= 1

        if y != num - 1 and t & 1 == 0:
            return False

    return True

# num桁のランダムな素数を生成する関数(mpnj()に依存)
def mkp(degit, k=100):
    if type(degit) is complex or type(k) is complex:
        return float("nan")
    if degit%1 != 0 or k%1 != 0 or degit < 1 or k < 1:
        return float("nan")

    num=random.randint(10**(degit-1),10**degit)
    while not mpnj(num, k):
        num=random.randint(10**(degit-1),10**degit)

    return num

# 軽い計算練習問題を出題する関数
def keisan(q_range = 10):

    # 整数入力関数 end, qまたはstopでキル
    def input_f(qestion_txt):
        result = 0
        while True:
            try:
                inputed = input(qestion_txt)
                result = int(inputed)

            except:
                if inputed == "end" or inputed == "stop" or inputed == "q":
                    return "kill"
                print("整数を入力してください。\nまた、関数を止めるときはendまたは、qを入力してください。")
                continue

            break
        return result


    # ジャッジ関数 (戻り値はポイント)
    def judge(ans1, ans2):
        if ans2 == "kill":
            return "kill"

        if ans1 == ans2:
            print("正解!\n")
            return 1

        else:
            print("不正解! 正解は{}\n".format(ans1))
            return 0


    # 演算子の後ろの数が負になっていいるときのカッコ
    def qestion_txt_miker(operator, x, y):
        if y < 0:
            return "{}{}({})=".format(x, operator, y)

        else:
            return "{}{}{}=".format(x, operator, y)


    # 足し算計算 (戻り値はポイント)
    def add(x, y):
        qestion_txt = qestion_txt_miker("+", x, y)
        ans = x+y
        inputed = input_f(qestion_txt)
        return judge(ans, inputed)


    # 引き算計算 (戻り値はポイント)
    def sub(x, y):
        qestion_txt = qestion_txt_miker("-", x, y)
        ans = x-y
        inputed = input_f(qestion_txt)
        return judge(ans, inputed)


    # 掛け算計算 (戻り値はポイント)
    def mult(x, y):
        qestion_txt = qestion_txt_miker("×", x, y)
        ans = x*y
        inputed = input_f(qestion_txt)
        return judge(ans, inputed)


    # 割り算計算 qrangeは問題に出る数の範囲の絶対値 (0割るのを防ぐため特殊化) (戻り値はポイント)
    def divi(qrange):
        x = randint(1, qrange)*(-1)**randint(1, 2)
        y = randint(1, qrange)*(-1)**randint(1, 2)
        product = x*y
        qestion_txt = qestion_txt_miker("÷", product, x)
        ans = y
        inputed = input_f(qestion_txt)
        return judge(ans, inputed)


    # メイン関数
    def keisan_main(times, qestion_range = 10):             # 問題数、問題出題範囲の絶対値(初期設定は-10~10まで)
        Score = 0                                           # 点数のフォーマット
        start_time = time.time()

        for i in range(1, times+1):
            print("Q.%d" %i)
            qestion_type = randint(0, 3)                    # 問題の演算子を決めるための数

            a = randint(-qestion_range, qestion_range)      # 出題するランダムな数を生成
            b = randint(-qestion_range, qestion_range)      # 出題するランダムな数を生成

            if qestion_type == 0:
                result = add(a, b)                          # 足し算の計算問題
            elif qestion_type == 1:
                result = sub(a, b)                          # 引き算の計算問題
            elif qestion_type == 2:
                result = mult(a, b)                         # 掛け算の計算問題
            else:
                result = divi(qestion_range)                # 割り算の計算問題

            if result == "kill":
                return "killed"
            else:
                Score += result

        end_time = time.time()
        time_required = round(end_time - start_time)

        if time_required < 60:
            time_required = "{}秒".format(time_required)
        elif time_required < 3600:
            time_required = "{}分{}秒".format(time_required//60, time_required%60)
        else:
            time_required = "{}時間{}分{}秒".format(time_required//3600, (time_required%3600)//60, (time_required%3600)%60)

        print("あなたのスコア: %d / %d" %(Score, times))
        print("問題にかかった時間: %s"%(time_required))
        return Score, (end_time-start_time)                  # 戻り値は点数とかかった時間

    times = input_f("計算する回数を入力:")
    if times == "kill":
        return "killed"

    return keisan_main(abs(times), q_range)

# メイン関数の補助機能なので改造は推奨しません。
class Computing_system:
    def log10(self, num):
        if num == 0:                                        # numが0のとき負の無限大を返す
            return -float("inf")
        return math.log10(abs(num))

    # 小数の扱いを決める関数
    def Format_converter(self, ans):
        if self.log10(ans) >= -12:
            if self.log10(ans) >= 12:
                return ans
            elif round(ans, 12) % 1 == 0:
                return round(ans)
            else:
                return round(ans, 12)
        else:
            return ans

    # 計算結果の誤差修正をする関数
    def Error_correction(self, ans):
        if type(ans) is complex:
            if (self.log10(ans.real) >= -12 or ans.real == 0) and round(ans.real, 12) == 0:
                return complex(0, self.Format_converter(ans.imag))
            elif round(ans.imag, 12) == 0:
                return self.Format_converter(ans.real)
            else:
                return complex(self.Format_converter(ans.real), self.Format_converter(ans.imag))

        elif type(ans) is float:
            if ans == float("inf"):
                return float("inf")
            elif ans == -float("inf"):
                return -float("inf")
            elif ans == float("nan"):
                return float("nan")
            else:
                return self.Format_converter(ans)
        return ans
system = Computing_system()

def main():
    print("Welcome! This is simple calculator.\nIf you want to watch demonstration, please type demo()\n")

    ans = 0
    preans = 0
    preans_cache = 0

    while True:
        Formula = str(input("> ")).replace("^", "**")
        try:
            ans = eval(Formula)
            preans_cache = ans
            preans = preans_cache
            print("%s" %(str(system.Error_correction(ans)).replace("j", "i")))

        except:
            try:
                exec(Formula)

            except:
                if Formula == "end" or Formula == "stop" or Formula == "q":
                    print("Stop the program", end="", flush=True)
                    for _ in range(3):
                        print(".", end="", flush=True)
                        time.sleep(0.25)
                    return 0

                print("Mathematical Error")
                continue
    return 0


if __name__ == "__main__":
    main()
