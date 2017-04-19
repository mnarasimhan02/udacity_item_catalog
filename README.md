##Fan Gear Shop Online Mangement

You can use this website to manage fan gear shops.

##Before running this website, make sure all the required python modules have been installed.
Please see Instructions.

##Instructions
1. Clone this project to your local machine at first.
3. Use `python database_setup.py` to create database.
4. Use `python import_fake_data.py` to import fake data if you want to test this website.
5. Use `python website.py` to run this website on your local machine.
6. Open browser and navigate to http://localhost:5000/

##Features
1. Using Flask ( a light Python web framework).
2. Using OAuth 2.0 to Access Google APIs.
	- You can login using your google account.
	- Only the owner can manage his own shop.
3. Using RESRfull APIs, like Post and Get.
4. Providing JSON APIs, which you can exploit to get the information you want.

## Also provides json APIs

#json APIs
@app.route('/index/<string:shop_ID>/JSON/')
def shopJSON(shop_ID):
    shops = session.query(fanShop).filter_by(id=shop_ID).one()
    fans = session.query(fanItem).filter_by(shop_id = shop_ID).all()
    return jsonify(Shop=shops.serialize, fans = [g.serialize for g in fans])


@app.route('/index/<string:shop_ID>/<string:fan_ID>/JSON/')
def fanJSON(shop_ID,fan_ID):
    fan = session.query(fanItem).filter_by(id=fan_ID).one()
    return jsonify(fan = fan.serialize)

You can use url likes `localhost:5000/index/<string:shop_ID>/JSON/` to get the JSON file corresponding to the shop with id = shop_ip; 
You can use url likes `localhost:5000/index/<string:shop_ID>/<string:Fan_ID>/JSON/` to get the JSON file corresponding to the Fan with id = Fan_ID. 

##You will see
The main page looks like:
![1](/screenshots/ScreenShot_1.png?raw=true)

You can use your google account to login:
![2](/screenshots/ScreenShot_2.png?raw=true)

You can create your own shop:
![3](/screenshots/ScreenShot_3.png?raw=true)

You can view the shop:
![4](/screenshots/ScreenShot_4.png?raw=true)

You can add new sport gear to your shop:
![5](/screenshots/ScreenShot_5.png?raw=true)

You can use JSON APIs like:
![6](/screenshots/ScreenShot_6.png?raw=true)
