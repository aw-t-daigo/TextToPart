# 概要

日本語の文章を書いたテキストを食わせると、品詞とその詳細だけのものになって出てきます

## 例

- before
```text
上野発の夜行列車 おりた時から
青森駅は 雪の中
北へ帰る人の群れは 誰も無口で
海鳴りだけを きいている
私もひとり 連絡船に乗り
こごえそうな鴎見つめ 泣いていました
ああ 津軽海峡冬景色
```

- after
```text
[名詞:固有名詞:地域][名詞:接尾:一般][助詞:連体化:][名詞:固有名詞:一般][動詞:自立:][助動詞::][名詞:非自立:副詞可能][助詞:格助詞:一般]
[名詞:固有名詞:一般][助詞:係助詞:][名詞:一般:][助詞:連体化:][名詞:非自立:副詞可能]
[名詞:一般:][助詞:格助詞:一般][動詞:自立:][名詞:一般:][助詞:連体化:][名詞:一般:][助詞:係助詞:][名詞:代名詞:一般][助詞:係助詞:][名詞:形容動詞語幹:][助動詞::]
[名詞:一般:][助詞:副助詞:][助詞:格助詞:一般][動詞:自立:][助詞:接続助詞:][動詞:非自立:]
[名詞:代名詞:一般][助詞:係助詞:][名詞:一般:][名詞:サ変接続:][名詞:接尾:一般][助詞:格助詞:一般][動詞:自立:]
[動詞:自立:][名詞:接尾:助動詞語幹][助動詞::][名詞:一般:][動詞:自立:][動詞:自立:][助詞:接続助詞:][動詞:非自立:][助動詞::][助動詞::]
[感動詞::][名詞:固有名詞:一般]
```

「上野発の夜行列車」は`[名詞:固有名詞:地域][名詞:接尾:一般][助詞:連体化:][名詞:固有名詞:一般]`に変換されます。

「発」は`[名詞:接尾:一般]`、「の」は`[助詞:連体化:]`に変換されていますね。

記号などは変換されません。

## 何に使うの？

こんなことの真似ができます

https://www.youtube.com/watch?v=8zjDhQC4MLQ

# 使い方

```shell
python main.py <ファイル名>
```
または
```shell
pipenv run cv <ファイル名>
```

# 準備

## 環境

- python 3.9
- mecab 0.996
- pipenv 2022.9.8

（推奨）
1. pyenv の導入
   1. `brew install pyenv`
   2. `pyenv local 3.9`

（必須）
1. pipenv の導入
   1. `pip install pipenv`
2. ライブラリのインストール
   1. `pipenv sync --dev`
3. MeCabと辞書のセット
   1. `brew install mecab`
   2. `cd mecab-ipadic-neologd`
   3. `./bin/install-mecab-ipadic-neologd -n`
      1. 途中`yes or no`を聞かれたら`yes`を選択
