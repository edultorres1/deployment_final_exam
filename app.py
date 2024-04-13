{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4f19e31e",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, request, jsonify, render_template\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "import io\n",
    "import base64\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "@app.route('/')\n",
    "def upload_file():\n",
    "    return render_template('upload.html')\n",
    "\n",
    "@app.route('/uploader', methods=['POST'])\n",
    "def uploader_file():\n",
    "    if 'file' not in request.files:\n",
    "        return \"No file part\"\n",
    "    file = request.files['file']\n",
    "    if file.filename == '':\n",
    "        return \"No selected file\"\n",
    "    if file:\n",
    "        # Read the file to a DataFrame\n",
    "        df = pd.read_csv(file)\n",
    "        \n",
    "        # Perform basic statistics\n",
    "        desc = df.describe()\n",
    "        \n",
    "        # Generate a histogram for the first numerical column as an example\n",
    "        plt.figure()\n",
    "        sns.histplot(df[df.columns[0]], kde=True)\n",
    "        hist_img = io.BytesIO()\n",
    "        plt.savefig(hist_img, format='png')\n",
    "        hist_img.seek(0)\n",
    "        plot_url = base64.b64encode(hist_img.getvalue()).decode('utf8')\n",
    "\n",
    "        return jsonify({\n",
    "            'description': desc.to_html(),\n",
    "            'histogram': f'<img src=\"data:image/png;base64,{plot_url}\"/>'\n",
    "        })\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run(debug=True, host='0.0.0.0', port=5000)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
