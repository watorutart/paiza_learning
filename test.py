# coding: utf-8

# 画像用ハッシュ
item_images = {
    "剣":"http://paiza.jp/learning/images/sword.png",
    "盾":"http://paiza.jp/learning/images/shield.png",
    "回復薬":"http://paiza.jp/learning/images/potion.png",
    "クリスタル":"http://paiza.jp/learning/images/crystal.png"
}

# アイテムの並び順配列
items_order = ["クリスタル", "盾", "剣", "回復薬", "回復薬", "回復薬"]

#print(items_order)
#print(item_images)

for item_name in items_order:
    print("<img src='"+item_images[item_name]+"'>")
    print(item_name+"<br>")
    
