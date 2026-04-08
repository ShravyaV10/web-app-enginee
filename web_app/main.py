from flask import Flask, render_template
app = Flask(__name__)
@app.route(&#39;/&#39;)
def home():
return render_template(&#39;index.html&#39;, title=&quot;Home Page&quot;)
if __name__ == &#39;__main__&#39;:
app.run(host=&#39;127.0.0.1&#39;, port=8080, debug=True)
