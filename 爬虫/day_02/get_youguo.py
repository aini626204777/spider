import re


# 获取网
html = """
<li >
<a class = "magazine_wrap" href = "https://www.ugirls.com/Shop/Detail/Product-212.html" target = "_blank" title = "[T012]尤果网圣诞特辑" >
<img class = "magazine_img lazy" src = "https://img.ugirls.tv/uploads/magazine/cover/7c57f29a610498244e468c58cbf822e7_cover_web_l.jpg" data-original = "https://img.ugirls.tv/uploads/magazine/cover/7c57f29a610498244e468c58cbf822e7_cover_web_l.jpg" alt = "[T012]尤果网圣诞特辑" width = "" height = "" style = "display: block;" >
<div class = "magazine_detail" >
<h1 class = "magazine_title" > [T012]尤果网圣诞特辑 < /h1 >
<div class = "magazine_other_info" >
<p > 发行时间/<span > 2015.12.23 07: 12: 32 < /span > </p >
<p > 订阅量/<span > 2050 < /span > </p >
</div >
<div class = "magazine_desp" >
尤果网圣诞嗨起来，这一次，我只想说，不得到你就会后悔。一次集                           					... < span class = "desp_over" > [详细] < /span >
</div >
</div >
</a >
<div class = "magazine_view" >
<a title = "订阅量" class = "icon-heart" > </a > <span class = "like_count" > 2050 < /span >
</div>
<div class="magazine_model_info">
<a href="https://www.ugirls.com/Models/Detail/Model-149.html" target="_blank" title="梓安"><img class="lazy" src="https://img.ugirls.tv/uploads/users/header/4b44e07935b3d3da87a60af1f2855905.jpg" data-original="https://img.ugirls.tv/uploads/users/header/4b44e07935b3d3da87a60af1f2855905.jpg" style="width: 26px; height: 26px; display: inline;" alt="梓安" width="26" height="26"></a>
<h1 class="magazine_model_name"><a href="https://www.ugirls.com/Models" target="_blank" title="模特">模特</a>/<a href="https://www.ugirls.com/Models/Detail/Model-149.html" target="_blank" title="梓安">梓安</a></h1>
<a class="magazine_tag" href="https://www.ugirls.com/Index/Search/Magazine-57.html" target="_blank" title="创意专辑">创意</a>
</div>
</li>
"""
# 构建一个正则匹配对象
pattern = re.compile('<img.*?magazine_img.*?src\s=\s"(.*?)".*?data-original.*?>', re.S)

result = re.findall(pattern,html)

# print(html)
print(result)