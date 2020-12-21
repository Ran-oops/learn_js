# ajax发送数据给python后端

## 一.前端参数和后端参数保持一致

![image-20201218182354507](https://github.com/Ran-oops/learn_js/edit/master/learn_js/img-folder/1.png)

![image-20201218182421736](C:\Users\93623\AppData\Roaming\Typora\typora-user-images\image-20201218182421736.png)

*为了保证取到值,traditional设为true*

![image-20201218182636336](C:\Users\93623\AppData\Roaming\Typora\typora-user-images\image-20201218182636336.png)

这两处的值一样才能取到值;

## 二. 后端处理完返回数据的方式

后台处理完返回数据使用`return HttpResponse(json.dumps(res))`





