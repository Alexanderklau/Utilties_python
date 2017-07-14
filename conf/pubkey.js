var apiurlLink = "http://127.0.0.1:8006";                                                    var apimklink = apiurlLink;
var apipicLink = "http://121.40.202.86:8005";
var apiBIAddress = 'http://118.178.88.203:8801';
var pagepurl = "http://127.0.0.1:8006/static/SaasWeb/";
var pageurl = pagepurl + "index.html#!"; //page页面地址
var rootPath = '/static/SaasWeb/';
var orgAccount = '';
var orgAccountCollection = '';
var regPwd = /^[0-9 | A-Z | a-z]{6,20}$/;
var regFloatNum = /^\d+(\.\d{0,2})?$/;
var pagesource = "";
var regPhone = /^(((1[0-9][0-9]{1}))+\d{8})$/; //电话号码正则表达式
var regPhoneFax = /^0\d{2,3}-\d{7,8}(-\d{1,10})?$/;
var regEmail = /^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$/;
var regQQ = /^\d+(\.\d+)?$/;
var regZipCode = /^[0-9]{6}$/;
var regNum = /^[0-9]*$/;
var regPhoneLength = 11;
var returnsource = "";
var valid_zmsz = /^(\w|[\u4E00-\u9FA5])*$/; /*支持中英文数字*/
var valid_ysz = /^[A-Za-z0-9_-]+$/; /*支持英文数字*/
var valid_zmszdian = /^(\w|[\u4E00-\u9FA5-\.])*$/; /*支持中英文数字、点*/
var valid_s = /^[1-9]+[0-9]*$/; /*支持自然数*/
var valid_date = /^(\d{4})-(\d{2})-(\d{2})$/; /*支持yyyy-mm-dd*/
var valid_number = /^-?[1-9]+(\.\d+)?$|^-?0(\.\d+)?$|^-?[1-9]+[0-9]*(\.\d+)?$/; /*支持数字包含小数点*/
var valid_numbersecond = /^\d+(\.\d{2})?$/; /*支持数字包含两位小数点*/

$(document).ready(function() {
	if(window.location.href.indexOf('login.html') < 0) {
		if(localStorage.userid == "" || localStorage.userid == null || localStorage.userid == undefined) {
			window.location.href = pagepurl + "login.html";
		} else {
			orgAccount = localStorage.orgAccount;
			orgAccountCollection = localStorage.orgAccount;
			/*localStorage.xgmm 修改密码，重新登录为0，未重新登录为1*/
			/*if(localStorage.xgmm == 1) {
				setTimeout(function() {
					ShowCfrims("密码修改成功,需要重新登录", "Loginout(),");
				}, 4000);
			}*/
		}
	}
});

function createXmlHttpRequest() {
	return window.XMLHttpRequest ? new XMLHttpRequest() : window.ActiveXObject ? new ActiveXObject("Microsoft.XMLHTTP") : new XMLHttpRequest();
}

function downloadJSAtOnload(URL) {
	var element = document.createElement("script");
	element.src = URL;
	document.body.appendChild(element);
}

/*angluar posturl*/
function aj_PostSend($http, urllink, datas, fn, contenttype) {
	ShowMsg("load", "努力加载中.....");
	$http({
		method: "POST",
		url: urllink,
		data: datas,
		headers: {
			'Content-Type': (contenttype != "" && contenttype != undefined && contenttype != null) ? contenttype : 'application/x-www-form-urlencoded'
		}
	}).success(function(result, status) {
		$(".loadding").remove();
		switch(status) {
			case 200:
				fn(result);
				break;
			default:
				ShowMsg("error", "稍等。。。正在处理中");
				break;
		}
	}).error(function() {
		$(".loadding").remove();
		ShowMsg("error", "稍等。。。正在处理中");
	});
}

function aj_getSend($http, datas, urllink, fn) {
	ShowMsg("load", "努力加载中.....");
	$http({
		method: "GET",
		url: urllink,
		data: datas
	}).success(function(result, status) {
		$(".loadding").remove();
		switch(status) {
			case 200:
				fn(result);
				break;
			default:
				ShowMsg("error", "稍等。。。正在处理中");
				break;
		}
	}).error(function() {
		$(".loadding").remove();
		ShowMsg("error", "稍等。。。正在处理中");
	});
}

function aj_getSend($http, urllink, fn) {
	ShowMsg("load", "努力加载中.....");
	$http.get(urllink).success(function(result, status) {
		$(".loadding").remove();
		switch(status) {
			case 200:
				if(fn) {
					fn(result);
				}
				break;
			default:
				ShowMsg("error", "稍等。。。正在处理中");
				break;
		}
	}).error(function() {
		$(".loadding").remove();
		ShowMsg("error", "稍等。。。正在处理中");
	});
}

function createXMLHttpRequest() {
	if(window.XMLHttpRequest) {
		return new XMLHttpRequest();
	} else {
		var MSXML = ['MSXML2.XMLHTTP.5.0', 'MSXML2.XMLHTTP.4.0', 'MSXML2.XMLHTTP.3.0', 'MSXML2.XMLHTTP', 'Microsoft.XMLHTTP'];
		for(var i = 0; n < MSXML.length; i++) {
			try {
				return new ActiveXObject(MSXML[i]);
				break;
			} catch(e) {
				console.log("创建XMLHttpRequest对象失败");
			}
		}
	}
}
/**
 * 通过post方式提交
 * */
function postSend(objXMLHttp, url, data, processResponse) {
	ShowMsg("load", "努力加载中.....");
	objXMLHttp.open("POST", url, true);
	objXMLHttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
	objXMLHttp.onreadystatechange = processResponse;
	objXMLHttp.send(data);
}

function postSend(objXMLHttp, url, data, processResponse, pfunc) {
	ShowMsg("load", "努力加载中.....");
	objXMLHttp.open("POST", url, true);
	objXMLHttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
	if(pfunc != null) {
		objXMLHttp.upload.addEventListener("progress", function(event) {
			if(event.lengthComputable) {
				percentComplete = Math.round(event.loaded * 100 / event.total);
			}
			pfunc(percentComplete);
		})
	}
	objXMLHttp.onreadystatechange = processResponse;
	objXMLHttp.send(data);
}

function PGSend_fd(objXMLHttp, method, url, data, processResponse, pfunc) {
	ShowMsg("load", "努力加载中.....");
	objXMLHttp.open(method, url, true);
	//objXMLHttp.setRequestHeader("Content-Type", "multipart/form-data");
	if(pfunc != null) {
		objXMLHttp.upload.addEventListener("progress", function(event) {
			if(event.lengthComputable) {
				percentComplete = Math.round(event.loaded * 100 / event.total);
			}
			pfunc(percentComplete);
		})
	}
	objXMLHttp.onreadystatechange = processResponse;
	objXMLHttp.send(data);
}
/**
 * 通过GET请求
 * */
function getSend(objXMLHttp, url, processResponse) {
	ShowMsg("load", "努力加载中.....");
	objXMLHttp.open("GET", url, true);
	objXMLHttp.onreadystatechange = processResponse;
	objXMLHttp.send(null);
}
/**
 * 设定的回调函数
 * */
function _processResponse(objXMLHttp, fn) {
	$(".loadding").remove();
	if(objXMLHttp.readyState == 4) {
		data = objXMLHttp.responseText;
		switch(objXMLHttp.status) {
			case 200:
				var _datajson = JSON.parse(data);
				fn(_datajson);
				break;
			case 403:
			case 500:
				BtnCancel();
				ShowMsg("error", "稍等。。。正在处理中");
				break;
		}
	}
}

//基于jquery的封装get/post请求
(function() {
	$.getJson = function(url, func) {
		ShowMsg("load", "努力加载中.....");
		$.ajax({
			url: url,
			type: "get",
			success: function(data) {
				$(".loadding").remove();
				func(data);
			},
			// success: func,
			error: function(res) {
				console.log("服务器出错了！！");
			}
		});
	};

	$.postJson = function(url, args, successCall, failCall, alwaysCall) {
		ShowMsg("load", "努力加载中.....");
		var req = $.ajax({
			url: url,
			type: "post",
			data: JSON.stringify(args),
			contentType: "application/x-www-form-urlencoded", //x-www-form-urlencoded json; charset=utf-8
			success: function(data) {
				$(".loadding").remove();
				successCall(data);
			},
			// success: successCall,
			fail: failCall,
			error: failCall
		});
		req.always(alwaysCall);
	};

	$.postForm = function(url, args, successCall, failCall, alwaysCall) {
		ShowMsg("load", "努力加载中.....");
		var req = $.ajax({
			url: url,
			type: "post",
			data: args,
			contentType: "application/x-www-form-urlencoded", //x-www-form-urlencoded json; charset=utf-8
			// dataType : "json",
			success: function(data) {
				$(".loadding").remove();
				successCall(data);
			},
			// success: successCall,
			fail: failCall,
			error: failCall
		});
		req.always(alwaysCall);
	};
})(jQuery);

/*card valid*/
function validateIdCard(idCard) {
	//15位和18位身份证号码的正则表达式
	var regIdCard = /^(^[1-9]\d{7}((0\d)|(1[0-2]))(([0|1|2]\d)|3[0-1])\d{3}$)|(^[1-9]\d{5}[1-9]\d{3}((0\d)|(1[0-2]))(([0|1|2]\d)|3[0-1])((\d{4})|\d{3}[Xx])$)$/;

	//如果通过该验证，说明身份证格式正确，但准确性还需计算
	if(regIdCard.test(idCard)) {
		if(idCard.length == 18) {
			var idCardWi = new Array(7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2); //将前17位加权因子保存在数组里
			var idCardY = new Array(1, 0, 10, 9, 8, 7, 6, 5, 4, 3, 2); //这是除以11后，可能产生的11位余数、验证码，也保存成数组
			var idCardWiSum = 0; //用来保存前17位各自乖以加权因子后的总和
			for(var i = 0; i < 17; i++) {
				idCardWiSum += idCard.substring(i, i + 1) * idCardWi[i];
			}

			var idCardMod = idCardWiSum % 11; //计算出校验码所在数组的位置
			var idCardLast = idCard.substring(17); //得到最后一位身份证号码

			//如果等于2，则说明校验码是10，身份证号码最后一位应该是X
			if(idCardMod == 2) {
				if(idCardLast == "X" || idCardLast == "x") {
					return 0;
				} else {
					return 1;
				}
			} else {
				//用计算出的验证码与最后一位身份证号码匹配，如果一致，说明通过，否则是无效的身份证号码
				if(idCardLast == idCardY[idCardMod]) {
					return 0;
				} else {
					return 1;
				}
			}
		}
	} else {
		return 1;
	}
}

/*Get the URL of the value parameter*/
function GetUrlParameter(paramName) {
	var returnVal = "";
	try {
		var paramUrl = window.location.search;
		if(paramUrl.length > 0) {
			paramUrl = paramUrl.substring(1, paramUrl.length);
			var paramUrlArray = paramUrl.split("&");
			for(var i = 0; i < paramUrlArray.length; i++) {
				if(paramUrlArray[i].toLowerCase().indexOf(paramName.toLowerCase()) != -1) {
					var temp = paramUrlArray[i].split("=");
					if(temp[0].toLowerCase() == paramName.toLowerCase()) {
						returnVal = temp[1];
						break;
					}
				}
			}
		}
	} catch(e) {}
	return returnVal;
}

/*bank vali*/
function luhmCheck(bankno) {
	var num = /^(\d{16}|\d{19})$/; //全数字
	if(!num.exec(bankno)) {
		return 0;
	}
	//开头6位
	var strBin = "10,18,30,35,37,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,58,60,62,65,68,69,84,87,88,94,95,98,99";
	if(strBin.indexOf(bankno.substring(0, 2)) == -1) {
		return 0;
	}
	var lastNum = bankno.substr(bankno.length - 1, 1); //取出最后一位（与luhm进行比较）

	var first15Num = bankno.substr(0, bankno.length - 1); //前15或18位
	var newArr = new Array();
	for(var i = first15Num.length - 1; i > -1; i--) { //前15或18位倒序存进数组
		newArr.push(first15Num.substr(i, 1));
	}
	var arrJiShu = new Array(); //奇数位*2的积 <9
	var arrJiShu2 = new Array(); //奇数位*2的积 >9

	var arrOuShu = new Array(); //偶数位数组
	for(var j = 0; j < newArr.length; j++) {
		if((j + 1) % 2 == 1) { //奇数位
			if(parseInt(newArr[j]) * 2 < 9)
				arrJiShu.push(parseInt(newArr[j]) * 2);
			else
				arrJiShu2.push(parseInt(newArr[j]) * 2);
		} else //偶数位
			arrOuShu.push(newArr[j]);
	}

	var jishu_child1 = new Array(); //奇数位*2 >9 的分割之后的数组个位数
	var jishu_child2 = new Array(); //奇数位*2 >9 的分割之后的数组十位数
	for(var h = 0; h < arrJiShu2.length; h++) {
		jishu_child1.push(parseInt(arrJiShu2[h]) % 10);
		jishu_child2.push(parseInt(arrJiShu2[h]) / 10);
	}

	var sumJiShu = 0; //奇数位*2 < 9 的数组之和
	var sumOuShu = 0; //偶数位数组之和
	var sumJiShuChild1 = 0; //奇数位*2 >9 的分割之后的数组个位数之和
	var sumJiShuChild2 = 0; //奇数位*2 >9 的分割之后的数组十位数之和
	var sumTotal = 0;
	for(var m = 0; m < arrJiShu.length; m++) {
		sumJiShu = sumJiShu + parseInt(arrJiShu[m]);
	}

	for(var n = 0; n < arrOuShu.length; n++) {
		sumOuShu = sumOuShu + parseInt(arrOuShu[n]);
	}

	for(var p = 0; p < jishu_child1.length; p++) {
		sumJiShuChild1 = sumJiShuChild1 + parseInt(jishu_child1[p]);
		sumJiShuChild2 = sumJiShuChild2 + parseInt(jishu_child2[p]);
	}
	//计算总和
	sumTotal = parseInt(sumJiShu) + parseInt(sumOuShu) + parseInt(sumJiShuChild1) + parseInt(sumJiShuChild2);

	//计算Luhm值
	var k = parseInt(sumTotal) % 10 == 0 ? 10 : parseInt(sumTotal) % 10;
	var luhm = 10 - k;

	if(lastNum == luhm) {
		return 1;
	} else {
		return 0;
	}
}

function ShowMsg(type, title) {
	if(type == "load") {
		ShowMsgLoad("<img src='" + pagepurl + "/assets/common/img/icon_tooltip_loading.png'/>" + title);
	} else {
		ShowMsg_info("<img src='" + pagepurl + "/assets/common/img/icon_tooltip_warning.png'/>" + title);
	}
}

function ShowMsg_info(msg) {
	var str = "<div class='information_box loaderrorinfo'>";
	str += "<div class='information_border'>";
	str += "<div class='information_Info'>";
	str += msg + "</div></div></div>";
	$("body").append(str);
	$(".loaderrorinfo").fadeIn(500, function() {
		setTimeout(function() {
			$(".loaderrorinfo").fadeOut(500, function() {
				$(".loaderrorinfo").remove();
			});
		}, 2000);
	});

}

function ShowMsgLoad(msg) {
	var str = "<div class='information_box loadding'>";
	str += "<div class='information_border'>";
	str += "<div class='information_Info'>";
	str += msg + "</div></div></div>";
	$("body").append(str);
}

function ShowMsg_ZMPic(msg, msid) {
	var str = "<div class=\"information_box zmpicloadding\">";
	str += "<div class=\"information_border\">";
	str += "<div class=\"information_Info\">";
	str += "<img src=\"" + pagepurl + "/assets/common/img/close.png\" class=\"imgclose\" onclick=\"btnCancelZmpic('" + msid + "')\"/>";
	str += "<div>" + msg + "</div>";
	str += "</div>";
	str += "</div>";
	str += "</div>";
	$("body").append(str);
}

function ShowConfrim(str1, str2, strname, btnconfrim) {
	var str = "<div class=\"confrim_box\">";
	str += "</div>";
	str += "<div class=\"confrim_winbox\">";
	str += "<div class=\"confrim_win_border\">";
	str += "<div class=\'confrim_win\'>";
	str += "<h4>" + str1 + "</h4>";
	str += "<h6>" + str2 + "</h6>";
	str += "<div class=\"margintop40\">";
	str += "<button type=\"button\" class=\"btn btn-danger  btn-lg margin-r-20\" onclick=\"" + btnconfrim + "\">确认" + strname + "</button>";
	str += "<button type=\"button\" class=\"btn btn-b7bde2 btn-lg\" id=\"btncancel\" onclick=\"BtnCancel()\">取消</button>";
	str += "</div>";
	str += "</div>";
	str += "</div>";
	str += "</div>";
	$("body").append(str);

}

function ShowCfrim(str1) {
	var str = "<div class=\"confrim_box\">";
	str += "</div>";
	str += "<div class=\"confrim_winbox\">";
	str += "<div class=\"confrim_win_border\">";
	str += "<div class=\'confrim_win\'>";
	str += "<h4>" + str1 + "</h4>";
	str += "<div class=\"margintop40\">";
	str += "<button type=\"button\" class=\"btn btn-danger btn-lg\" id=\"btncancel\" onclick=\"BtnCancel()\">确定</button>";
	str += "</div>";
	str += "</div>";
	str += "</div>";
	str += "</div>";
	$("body").append(str);
}

function ShowCfrims(str1, btn) {
	var str = "<div class=\"confrim_box\">";
	str += "</div>";
	str += "<div class=\"confrim_winbox\">";
	str += "<div class=\"confrim_win_border\">";
	str += "<div class=\'confrim_win\'>";
	str += "<h4>" + str1 + "</h4>";
	/*str += "<h6>" + str2 + "</h6>";*/
	str += "<div class=\"margintop40\">";
	str += "<button type=\"button\" class=\"btn btn-danger btn-lg\" id=\"btncancel\" onclick=\"" + btn + "BtnCancel()\">确定</button>";
	str += "</div>";
	str += "</div>";
	str += "</div>";
	str += "</div>";
	$("body").append(str);
}

function BtnCancel() {
	$(".confrim_box").remove();
	$(".confrim_winbox").remove();
}

function aj_ShowCfrim(str1, caitnier, btn) {
	var str = "<div class=\"confrim_box\">";
	str += "</div>";
	str += "<div class=\"confrim_winbox\">";
	str += "<div class=\"confrim_win_border\">";
	str += "<div class=\'confrim_win\'>";
	str += "<h4>" + str1 + "</h4>";
	str += "<div class=\"margintop40\">";
	str += "<button type=\"button\" class=\"btn btn-danger btn-lg\" id=\"btncancel\" onclick=\"" + btn + "\">确定</button>";
	str += "</div>";
	str += "</div>";
	str += "</div>";
	str += "</div>";
	$("" + caitnier + "").append(str);
}

function aj_ShowConfrim(caitnier, str1, str2, strname, btnconfrim) {
	var str = "<div class=\"confrim_box\">";
	str += "</div>";
	str += "<div class=\"confrim_winbox\">";
	str += "<div class=\"confrim_win_border\">";
	str += "<div class=\'confrim_win\'>";
	str += "<h4>" + str1 + "</h4>";
	str += "<h6>" + str2 + "</h6>";
	str += "<div class=\"margintop40\">";
	str += "<button type=\"button\" class=\"btn btn-danger  btn-lg margin-r-20\" onclick=\"" + btnconfrim + "\">确认" + strname + "</button>";
	str += "<button type=\"button\" class=\"btn btn-b7bde2 btn-lg\" id=\"btncancel\" onclick=\"BtnCancel()\">取消</button>";
	str += "</div>";
	str += "</div>";
	str += "</div>";
	str += "</div>";
	$("" + caitnier + "").append(str);
}

function picurl_newopen(url) {
	window.open(url);
}

function Tabs(pname, name) {
	var apply_status = $("#apply_status").val();
	var len = $("#tabs").find("li").length;
	if(name == ("tab" + len)) {
		BtnNext(name);
	} else {
		var none = $('#' + name).find(".buttonsave").css("display");
		if(none == "none") {
			$('#' + name).find(".btnedit").removeClass("displaynone")
		}
		var index = -1;
		if($("#" + name).find(".querydata").length) {
			index = $("#" + name).find(".querydata").html().indexOf('通话详单已提交');
		}
		if(index > -1) {
			$('#' + name).find(".querydata").removeClass("displaynone");
			$('#' + name).find(".editdata").addClass("displaynone");
			$('#' + name).find(".btnedit").removeClass("displaynone");
			$('#' + name).find(".buttonsave").addClass("displaynone")
			$('#' + name).find(".btncancel").addClass("displaynone")
		}
		$("#btnallaubit").addClass("displaynone");
		$('.' + pname).removeClass('divactive');
		$('#' + name).addClass('divactive');
		if(apply_status >= 1 && apply_status <= 3) {
			$(".tab-pane").find(".editdata").addClass("displaynone");
			$(".tab-pane").find(".btnedit").addClass("displaynone");
			$(".tab-pane").find(".btncancel").addClass("displaynone");
			$(".tab-pane").find(".buttonsave").addClass("displaynone");
			$(".tab-pane").find(".btnedit").addClass("displaynone");

		}
	}
}

function Loginout() {
	localStorage.userid = "";
	window.location.href = pagepurl + "login.html";
}

// 响应式
function adapt(num) {
	// var width = window.innerWidth; $('#main-content').width()
	// 260 侧边导航宽度
	var width = window.innerWidth - 300;

	if(num) {
		width = num;
	}

	if(width < 900) {
		width = 900;
	}
	if(width > 1280) {
		width = 1280;
	}
	window.contentWidth = width;
	//console.log(width);
	document.querySelector('html').style.fontSize = (width / 1050) * 100 + 'px';
}
/*文本框字符验证长度*/
function checktxtWord_len(c) {
	var value = c.value;
	var newvalue = value.replace(/[^\x00-\xff]/g, "**");
	var count = newvalue.length;
	return count;
}
/*文本框字符限制自动截取*/
function checktxtWord(c, byteLength) {
	var value = c.value;
	var newvalue = value.replace(/[^\x00-\xff]/g, "**");
	var length = newvalue.length;
	/*当输入文字的字节数小于设定的字节数*/
	if(length * 1 <= byteLength * 1) {
		return;
	}
	var limitDate = newvalue.substr(0, byteLength);
	var count = 0;
	var limitvalue = "";
	for(var i = 0; i < limitDate.length; i++) {
		var flat = limitDate.substr(i, 1);
		if(flat == "*") {
			count++;
		}
	}
	var size = 0;
	var istar = newvalue.substr(byteLength * 1 - 1, 1); /*校验点是否为“×”*/
	/*if 基点是×; 判断在基点内有×为偶数还是奇数*/
	if(count % 2 == 0) {
		/*当为偶数时*/
		size = count / 2 + (byteLength * 1 - count);
		limitvalue = value.substr(0, size);
	} else {
		/*当为奇数时*/
		size = (count - 1) / 2 + (byteLength * 1 - count);
		limitvalue = value.substr(0, size);
	}
	c.value = limitvalue;
	/*console.log("最大输入" + byteLength + "个字节（相当于" + byteLength / 2 + "个汉字）！");*/
	return;
}

/*日期+天数得到新日期*/
function getNewDay(dateTemp, days) {
	var dateTemp = dateTemp.split("-");
	var nDate = new Date(dateTemp[1] + '-' + dateTemp[2] + '-' + dateTemp[0]); //转换为MM-DD-YYYY格式    
	var millSeconds = Math.abs(nDate) + (days * 24 * 60 * 60 * 1000);
	var rDate = new Date(millSeconds);
	var year = rDate.getFullYear();
	var month = rDate.getMonth() + 1;
	if(month < 10) month = "0" + month;
	var date = rDate.getDate();
	if(date < 10) date = "0" + date;
	return(year + "-" + month + "-" + date);
}

/*屏蔽电话号码中间的四位数字*/
function hiddentel($phone) {
	if($phone != "" && $phone != null && $phone != undefined) {
		return $phone.replace(/(\d{3})(\d{4})(\d{4})/, "$1****$3")
	} else {
		return $phone;
	}
}
