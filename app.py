{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "1cd301a3",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, request, render_template"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "97181755",
   "metadata": {},
   "outputs": [],
   "source": [
    "import joblib"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "59f61812",
   "metadata": {},
   "outputs": [],
   "source": [
    "app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "4d4737fb",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route(\"/\", methods=[\"GET\",\"POST\"])\n",
    "def index():\n",
    "    if request.method==\"POST\":\n",
    "        beta = float(request.form.get(\"beta\"))\n",
    "        print(beta)\n",
    "        model1 = joblib.load(\"regression\")\n",
    "        r1 = model1.predict([[beta]])\n",
    "        model2 = joblib.load(\"tree\")\n",
    "        r2 = model2.predict([[beta]])\n",
    "        return(render_template(\"index.html\", result1=r1, result2=r2))\n",
    "    else:\n",
    "        return(render_template(\"index.html\", result1=\"waiting\", result2=\"waiting\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "f5809f5d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "   WARNING: This is a development server. Do not use it in a production deployment.\n",
      "   Use a production WSGI server instead.\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)\n"
     ]
    }
   ],
   "source": [
    "if __name__ == \"__main__\":\n",
    "    app.run()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "71beb2e9",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
