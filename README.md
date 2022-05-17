# tradingview-bitflyer-strategy-alert2
  
**BitflyerAPIとTradingviewのWebhookを繋げ売買の自動化を行います。**
 
# DEMO
 
Tradingviewから送信したWebhookを当サイトで受け取り、売買情報をAPIでPOSTします。
 
# Features
 
今までは、トレーディングアプリを用いて、価格情報などをGETし、データベースに格納し、ストラテジーを当てはめていましたが、多様なプラットフォームの登場により、売買のPOSTのみになりました。
 
# Requirement
 
ccxt==1.82.74
Flask==2.1.2
gunicorn==20.1.0
 
# Installation

pip install flask
pip install ccxt
pip install gunicorn
 
# Usage
  
```bash
git clone https://github.com/~~~~~
cd 当ディレクトリ
python app.py
```
ローカル環境では、コメントアウトを外してください。
 
# Note
 
 
まず参考にしたYoutubechennelがあります。まず、こちらをご覧ください。
https://www.youtube.com/watch?app=desktop&v=gMRee2srpe8

もし間違っている点や、省略可能なところがございましたら、ご教授のほど宜しくお願いします。
APIkeyなどは既に無効化しております。

また、売買に生じるコストや損益は、責任を負いません。<br>
また、セキュリティなどに関しては、責任を負いません。<br>
また、最終的な投資決定は、お客さまご自身の判断でなさるようにお願いいたします。<br>
また、現在は、buy or sellのみdataを与えていますが、PinescriptやPythonでは様々なやり方があるはずですので、ご自身で変更をお願いします。<br>
また、Tradingviewのwebhookでは、30秒ほど遅延が起こります。これはTradingview側のプランによってスピードが変わる設定になっています。ご自身で変更をお願いします。Premiumでは3秒ほどの遅延が生じます。<br>
また、PythonでRealtimeTickerを取得し、売買する方法もございます。そちらの方が、売買の高速化は可能です。<br>
また、herokuでのデプロイでは、上記Youtuberを参考にし、Procfileファイルを作成する必要があります。<br>
また、herokuでのデプロイでは、requirements.txtが必要です。<br>
また、heroku自体、開くまでが遅いですので、デイからスイング以降がよろしいかと思われます。<br>

 
# License
ライセンスを明示する
 
This is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).
