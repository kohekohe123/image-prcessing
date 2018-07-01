# image-prcessing
初めてのgithub
(movie.py)
cv2.VideoCapture() で VideoCapture オブジェクトを取得する。 引数にはコンピュータに接続されているカメラの番号を指定しており、コンピュータにカメラが1台だけしか接続されていない場合には「0」を指定し、複数のカメラが接続されている場合は「1」などの番号を指定する。while文で繰り返すことでカメラから連続的に画像を取得する。 while 内の最初で、カメラから1コマのデータを取得するため capture.read() を呼び出して、取得した画像データを変数 frameに代入している。
OpenCV には、OSのフレーム(ウィンドウ)に画像を表示してくれる cv2.imshow() メソッドがあり、これを呼び出すと自動的にフレーム(ウィンドウ)が立ち上がって画像を表示する。

参考文献　https://weblabo.oscasierra.net/python/opencv-videocapture-camera.html

(gray_movie.py)
cv2.createTrackbar("ON/OFF","gray", 0, 1, myfunc)とすることで、インタラクティブにグレースケール動画に変更できるようにしている。なお、グレースケールへの変換はgray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)によって行っている。

(color_movie.py)
これもインタラクティブにしている。読み込んだ画像のチャネルをそれぞれ取り出し、γ変換をして元に戻し連続的に表示させている。なお、γ変換の際に0で割ってしまうことのないようにif文で制限している。

(filter_movie.py)
フィルタをかけるかどうかをインタラクティブに実行できる。4近傍のラプラシアンフィルタを実装している。読み込んだ画像をconvolve(gray,lf)により、畳み込みで計算してフィルタをかけている。
