from tools.api import request_tool
'''
自动生成 数字 20,80   #生成20到80之间的数字 例：56
自动生成 字符串 5 中文数字字母特殊字符 xuepl        #生成以xuepl开头加上长度2到5位包含中文数字字母特殊字符的字符串，例子：xuepl我1
自动生成 地址
自动生成 姓名
自动生成 手机号
自动生成 邮箱
自动生成 身份证号
'''
#创建商品
def test_addProd(pub_data):
    pub_data["productCode"] = "自动生成 字符串 2 数字 sb"
    method = "POST"  #请求方法，全部大写
    feature = "商品模块"  # allure报告中一级分类
    story = '创建商品'  # allure报告中二级分类
    title = "创建商品_全字段正常流_1"  # allure报告中用例名字
    uri = "/product/addProd"  # 接口地址
    header = {"token": pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    json_data='''{
  "brand": "耐克",
  "colors": [
    "黑色","白色"
  ],
  "price": 200,
  "productCode": "${productCode}",
  "productName": "裤子",
  "sizes": [
    "s","m"
  ],
  "type": "服装"
}'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=header,expect=expect,feature=feature,story=story,title=title,json_data=json_data)

#修改产品的状态测试下架
def test_soldOut(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "商品模块"  # allure报告中一级分类
    story = '产品下架'  # allure报告中二级分类
    title = "产品下架_全字段正常流_1"  # allure报告中用例名字
    uri = "/product/soldOut"  # 接口地址
    headers = {"token": pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    data={'productCode': '${productCode}'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,data=data)

# 修改产品的状态测试预售
def test_soldOut(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "商品模块"  # allure报告中一级分类
    story = '产品预售'  # allure报告中二级分类
    title = "产品预售_全字段正常流_1"  # allure报告中用例名字
    uri = "/product/toPreSale"  # 接口地址
    headers = {"token": pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    data={'productCode': '${productCode}'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,data=data)

def test_3(pub_data):
    method = "GET"  #请求方法，全部大写
    feature = "商品模块"  # allure报告中一级分类
    story = '根据条件查询商品'  # allure报告中二级分类
    title = "根据条件查询商品_全字段正常流_1"  # allure报告中用例名字
    uri = "/product/getSKU/1/3"  # 接口地址
    headers = {"token": pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    params={'endTime': '2018-10-19 10:41:18', 'startTime': '2018-10-18 09:41:18', 'status': '2'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,params=params)