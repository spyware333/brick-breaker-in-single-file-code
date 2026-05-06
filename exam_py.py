{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMSmoswOGr2Lcg7mfutLwXL",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/spyware333/brick-breaker-in-single-file-code/blob/main/exam_py.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "Rx59rnpgEmUu"
      },
      "outputs": [],
      "source": [
        "import numpy as np\n",
        "import pandas as pd"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df = pd.read_csv(\"/content/sales.csv\", index_col=[\"product_name\"])\n",
        "print(df)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pqtpZHPXE8Fw",
        "outputId": "0531a5dd-6ee2-4dc6-9f7e-f9abd106d52e",
        "collapsed": true
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "                category  price  quantity_sold       day\n",
            "product_name                                            \n",
            "Bread          Groceries     50             45  Saturday\n",
            "Milk               Dairy    120             32  Saturday\n",
            "Chicken             Meat    350             12  Saturday\n",
            "Apple             Fruits     80             28  Saturday\n",
            "Rice           Groceries    180             18  Saturday\n",
            "Bread          Groceries     50             40    Sunday\n",
            "Milk               Dairy    120             35    Sunday\n",
            "Chicken             Meat    350             10    Sunday\n",
            "Apple             Fruits     80             32    Sunday\n",
            "Rice           Groceries    180             20    Sunday\n",
            "Bread          Groceries     50             38    Monday\n",
            "Milk               Dairy    120             30    Monday\n",
            "Chicken             Meat    350             14    Monday\n",
            "Apple             Fruits     80             25    Monday\n",
            "Rice           Groceries    180             16    Monday\n",
            "Yogurt             Dairy     90             28  Saturday\n",
            "Yogurt             Dairy     90             25    Sunday\n",
            "Yogurt             Dairy     90             22    Monday\n",
            "Tomato        Vegetables     60             40  Saturday\n",
            "Tomato        Vegetables     60             38    Sunday\n",
            "Tomato        Vegetables     60             35    Monday\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df['money_earned'] = df['price'] * df['quantity_sold']\n",
        "money_per_day = df.groupby('day')['money_earned'].sum()\n",
        "print(money_per_day)\n",
        "total_money_earned = money_per_day.sum()\n",
        "print(f\"Total money earned: {total_money_earned}\")"
      ],
      "metadata": {
        "id": "dGP-9L5mF_YP",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "outputId": "1552fce5-6e4e-46dd-d3bb-82c99db13967"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "day\n",
            "Monday      19360\n",
            "Saturday    20690\n",
            "Sunday      20390\n",
            "Name: money_earned, dtype: int64\n",
            "Total money earned: 60440\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df[\"product_sum\"] = df['price'] * df['quantity_sold']\n",
        "product_total = df.groupby(\"product_name\")[\"product_sum\"].sum()\n",
        "print(product_total)\n",
        "product_sum = product_total.sum()\n",
        "print(f\"Total sum of all products: {product_sum}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "0wEdC7cnprut",
        "outputId": "070b1f1a-6064-4565-e3ea-b4cdf6820e02"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "product_name\n",
            "Apple       6800\n",
            "Bread       6150\n",
            "Chicken    12600\n",
            "Milk       11640\n",
            "Rice        9720\n",
            "Tomato      6780\n",
            "Yogurt      6750\n",
            "Name: product_sum, dtype: int64\n",
            "Total sum of all products: 60440\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "61ae8278",
        "outputId": "f59d46c8-d9b0-49dc-bef8-992509be4537"
      },
      "source": [
        "category_sales = df.groupby('category')['money_earned'].sum()\n",
        "print(category_sales)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "category\n",
            "Dairy         18390\n",
            "Fruits         6800\n",
            "Groceries     15870\n",
            "Meat          12600\n",
            "Vegetables     6780\n",
            "Name: money_earned, dtype: int64\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "J3uR7L8I8ep9"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}