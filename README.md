# Twitter の名前に天気絵文字付けるやつ

n 番煎じのやつです。
天気絵文字を現在の天気絵文字に書き換えるやつです。
[作ったやつ](https://twitter-weather-screen-name.herokuapp.com/)

## 処理の流れ

### 認証

認証処理用に flask でうごかしてる

1. Twitter 認証ヘリダイレクト
2. 返ってきたら、アクセストークンを取得
3. アクセストークンを DB に保存
4. Twitter にリダイレクト

## バッチ処理

Heroku Scheduler での最小実行単位(10 分)で実行

1. DB から登録されたトークンを取得
2. トークンから Twitter 名を取得
3. 登録された地名から座標を GoogleMapGeoCoording で取得
4. 座標から天気を OpenWeatherMap で取得
5. 名前に天気絵文字が含まれている場合、現在の天気絵文字に書き換える

## 次やるなら

- 認証・連携を Firebase に任せる
- flask・django の場合、oauth 系ライブラリを使う
