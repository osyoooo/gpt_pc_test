import streamlit as st # フロントエンドを扱うstreamlitの機能をインポート
import openai # openAIのchatGPTのAIを活用するための機能をインポート
import time

# アクセスの為のキーをopenai.api_keyに代入し、設定
# ここにご自身のAPIキーを入力してください！
openai.api_key = st.secrets["openaikey"]

content_kind_of =[
    "中立的で客観的な文章でしっかりした説明つきの文章",
    "分かりやすい、簡潔な文章",
    # "親しみやすいトーンの文章",
    # "専門用語をできるだけ使わない、一般読者向けの文章",
    # "言葉の使い方にこだわり、正確な表現を心がけた文章",
    # "ユーモアを交えた文章",
    "シンプルかつわかりやすい文法を使った文章",
    # "面白く、興味深い内容を伝える文章",
    "具体的でイメージしやすい表現を使った文章",
    # "人間味のある、感情や思いを表現する文章",
    "引用や参考文献を適切に挿入した、信頼性の高い文章",
    # "読み手の興味を引きつけるタイトルやサブタイトルを使った文章",
    "統計データや図表を用いたわかりやすく、しっかりとした説明つきの文章",
    "統計データや図表を用いたわかりやすい文章",
    # "独自の見解や考え方を示した、論理的な文章",
    # "問題提起から解決策までを網羅した、解説的な文章",
    # "ニュース性の高い、旬なトピックを取り上げた文章",
    #  "エンターテイメント性のある、軽快な文章",
    #  "読者の関心に合わせた、専門的な内容を深く掘り下げた文章",
    # "人物紹介やインタビューを取り入れた、読み物的な文章",
]

# chatGPTにリクエストするためのメソッドを設定。引数には書いてほしい内容と文章のテイストと最大文字数を指定
def run_gpt(content_text_to_gpt_mokuteki,content_text_to_gpt_pc1,content_text_to_gpt_pc2,content_text_to_gpt_pc3,content_kind_of_to_gpt):
    # リクエスト内容を決める
    request_to_gpt = "次の３台のパソコンのスペックを比較して、一番おススメのパソコンの型番と名称を回答の一番上に表示してください。なお、主な利用用途は" + content_text_to_gpt_mokuteki + "です。" + "１つ目のパソコンは" + content_text_to_gpt_pc1 + "２つ目のパソコンは" + content_text_to_gpt_pc2 + "３つ目のパソコンは" + content_text_to_gpt_pc3 + "です。また、文章は" + content_kind_of_to_gpt + "にしてください。"
    
    # 決めた内容を元にopenai.ChatCompletion.createでchatGPTにリクエスト。オプションとしてmodelにAIモデル、messagesに内容を指定
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": request_to_gpt },
        ],
    )

    # 返って来たレスポンスの内容はresponse.choices[0]["message"]["content"].strip()に格納されているので、これをoutput_contentに代入
    output_content = response.choices[0]["message"]["content"].strip()
    return output_content # 返って来たレスポンスの内容を返す

    #時間の提議
    time.sleep(5)  # 5秒待つ
    return "処理が完了しました！"

st.title('GPTにPCのスペックを比較してもらうアプリ')# タイトル

# 書かせたい内容
content_text_to_gpt_mokuteki = st.sidebar.text_input("PCの主な利用用途を教えてください")
content_text_to_gpt_pc1 = st.sidebar.text_input("１つ目のPC情報を入力してください")
content_text_to_gpt_pc2 = st.sidebar.text_input("2つ目のPC情報")
content_text_to_gpt_pc3 = st.sidebar.text_input("3つ目のPC情報")
            
# 書かせたい内容のテイストを選択肢として表示する
content_kind_of_to_gpt = st.sidebar.selectbox("文章の種類",options=content_kind_of)

# 「実行」ボタンが押されたら、run_gpt関数を実行する　処理中にメッセージと画像を表示する

if st.sidebar.button('実行'):
    with st.empty():
        # 処理中の画像を表示
        st.image("https://assets.st-note.com/production/uploads/images/112078423/5d47fc150315f1fa27c5efed19c704c9.png?crop=1.6%3A0.27&quality=60&quot;")
        st.markdown("### 処理中です...")
        
        output_content_text = run_gpt(content_text_to_gpt_mokuteki, content_text_to_gpt_pc1, content_text_to_gpt_pc2, content_text_to_gpt_pc3, content_kind_of_to_gpt)
        
    st.success('処理が完了しました！')
    st.write(output_content_text)
else:
    st.write("サイドバーの項目を入力し、「実行」ボタンを押してください。")