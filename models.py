import mysql.connector


shajeerdata= mysql.connector.connect(
    host="localhost", user="root", password="", database="finsys_tkinter", port="3306"
)
shajeercursor=shajeerdata.cursor()

shajeerdata.execute("""
                    create table inventory(
                    inventoryid int AUTO_INCREMENT, 
                    cid int,
                    image ImageField(upload_to'img/', default'/images/default.png'),
                    name varchar(100),
                    sku  varchar(100),
                    hsn  varchar(100),
                    unit varchar(100),
                    category varchar(100),
                    initialqty varchar(100),
                    date varchar(100),
                    stockalrt varchar(100),
                    invacnt varchar(100),
                    description varchar(100),
                    salesprice varchar(100),   
                    incomeacnt varchar(100),
                    tax  varchar(100),
                    purchaseinfo varchar(100),
                    cost  CharField100),
                    expacnt  CharField100),
                    purtax  CharField100),
                    revcharge  CharField100),
                    presupplier  CharField100),
                    cxq  FloatField(default=0.0, null=True)

                """)

shajeerdata.execute("""
                 create table noninventory(
                    noninventoryid int AUTO_INCREMENT, 
                    cid int,
                    image ImageField(upload_to'img/', default'/images/default.png'),
                    name varchar(100),
                    sku  varchar(100),
                    hsn  varchar(100),
                    unit varchar(100),
                    category varchar(100),
                    initialqty varchar(100),
                    date varchar(100),
                    stockalrt varchar(100),
                    invacnt varchar(100),
                    description varchar(100),
                    salesprice varchar(100),   
                    incomeacnt varchar(100),
                    tax  varchar(100),
                    purchaseinfo varchar(100),
                    cost  CharField100),
                    expacnt  CharField100),
                    purtax  CharField100),
                    revcharge  CharField100),
                    presupplier  CharField100),
                    qty varchar(100, default='0')

                """)


shajeerdata.execute("""
                 create table bundle(
                     
                    bundleid int AUTO_INCREMENT,
                    cid varchar(100),
                    image ImageField(upload_to="img/%y"),
                    name varchar(100),
                    sku varchar(100),
                    description varchar(100)
                    product1 varchar(100, default="", null=True),
                    product2 varchar(100, default="", null=True),
                    product3 varchar(100, default="", null=True),
                    product4 varchar(100, default="", null=True),
                    hsn1 varchar(100, default="", null=True),
                    hsn2 varchar(100, default="", null=True),
                    hsn3 varchar(100, default="", null=True),
                    hsn4 varchar(100, default="", null=True),
                    description1 varchar(255, default="", null=True),
                    description2 varchar(255, default="", null=True),
                    description3 varchar(255, default="", null=True),
                    description4 varchar(255, default="", null=True),
                    qty1 IntegerField(default=0, null=True),
                    qty2 IntegerField(default=0, null=True),
                    qty3 IntegerField(default=0, null=True),
                    qty4 IntegerField(default=0, null=True),
                    price1 FloatField(default=0.0, null=True),
                    price2 FloatField(default=0.0, null=True),
                    price3 FloatField(default=0.0, null=True),
                    price4 FloatField(default=0.0, null=True),
                    total1 FloatField(default=0.0, null=True),
                    total2 FloatField(default=0.0, null=True),
                    total3 FloatField(default=0.0, null=True),
                    total4 FloatField(default=0.0, null=True),
                    tax1 FloatField(default=0.0, null=True),
                    tax2 FloatField(default=0.0, null=True),
                    tax3 FloatField(default=0.0, null=True),
                    tax4 FloatField(default=0.0, null=True),
                    grandtotal FloatField(default=0.0, null=True)

                """)

shajeerdata.execute("""
                 create table services(
                    searviceid int AUTO_INCREMENT, 
                    cid int,
                    image ImageField(upload_to'img/', default'/images/default.png'),
                    name varchar(100),
                    sku  varchar(100),
                    hsn  varchar(100),
                    unit varchar(100),
                    category varchar(100),
                    initialqty varchar(100),
                    date varchar(100),
                    stockalrt varchar(100),
                    invacnt varchar(100),
                    description varchar(100),
                    salesprice varchar(100),   
                    incomeacnt varchar(100),
                    tax  varchar(100),
                    purchaseinfo varchar(100),
                    cost  CharField100),
                    expacnt  CharField100),
                    purtax  CharField100),
                    revcharge  CharField100),
                    presupplier  CharField100)

                """)

