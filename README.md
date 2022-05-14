# tradingview-bitflyer-strategy-alert2
BitflyerAPIとTradingviewのWebhookを繋げ売買の自動化を行います。


まず参考にしたYoutubechennelがあります。まず、こちらをご覧ください
https://www.youtube.com/watch?app=desktop&v=gMRee2srpe8

２時間ほどで作成しましたが、(まだ無職アルバイターの転職活動中のペーペーエンジニアですので)、もし間違っている点や、省略可能なところがございましたら、ご教授のほど宜しくお願いします。
APIkeyなどは既に無効化しております。

また、売買に生じるコストは、責任を負いません。
また、セキュリティなどに関しては、責任を負いません。
また、最終的な投資決定は、お客さまご自身の判断でなさるようにお願いいたします。
また、現在は、buy or sellのみdataを与えていますが、PinescriptやPythonでは様々なやり方があるはずですので、ご自身で変更をお願いします。
また、Tradingviewのwebhookでは、30秒ほど遅延が起こります。これはTradingview側のプランによってスピードが変わる設定になっています。ご自身で変更をお願いします。Premiumでは3秒ほどの遅延が生じます。
また、PythonでRealtimeTickerを取得し、売買する方法もございます。そちらの方が、売買の高速化は、可能です。
また、
