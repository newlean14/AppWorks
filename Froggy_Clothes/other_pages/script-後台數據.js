// 獲取所有側邊欄功能表項目的連結元素
const allSideMenu = document.querySelectorAll('#sidebar .side-menu.top li a');

// 為每個功能表項目添加點擊事件監聽器
allSideMenu.forEach(item => {
	const li = item.parentElement;

	item.addEventListener('click', function () {
		// 移除所有功能表項目的活動狀態
		allSideMenu.forEach(i => {
			i.parentElement.classList.remove('active');
		})
		// 添加當前功能表項目的活動狀態
		li.classList.add('active');
	})
});

// 切換側邊欄的顯示和隱藏
const menuBar = document.querySelector('#content nav .bx.bx-arrow-from-right');
const sidebar = document.getElementById('sidebar');

menuBar.addEventListener('click', function () {
	sidebar.classList.toggle('hide');
	// 切換箭頭圖示
	menuBar.classList.toggle('bx-arrow-from-right');
	menuBar.classList.toggle('bx-arrow-to-right');
})

// 搜索按鈕和搜索表單的交互效果
const searchButton = document.querySelector('#content nav form .form-input button');
const searchButtonIcon = document.querySelector('#content nav form .form-input button .bx');
const searchForm = document.querySelector('#content nav form');

searchButton.addEventListener('click', function (e) {
	// 在小螢幕上阻止預設點擊行為
	if (window.innerWidth < 576) {
		e.preventDefault();
		searchForm.classList.toggle('show');
		if (searchForm.classList.contains('show')) {
			searchButtonIcon.classList.replace('bx-search', 'bx-x');
		} else {
			searchButtonIcon.classList.replace('bx-x', 'bx-search');
		}
	}
})

// 根據視窗大小設置側邊欄、搜索按鈕和搜索表單的初始狀態
if (window.innerWidth < 768) {
	sidebar.classList.add('hide');
} else if (window.innerWidth > 576) {
	searchButtonIcon.classList.replace('bx-x', 'bx-search');
	searchForm.classList.remove('show');
}

// 監聽視窗大小變化事件，根據視窗大小調整搜索按鈕和搜索表單的狀態
window.addEventListener('resize', function () {
	if (this.innerWidth > 576) {
		searchButtonIcon.classList.replace('bx-x', 'bx-search');
		searchForm.classList.remove('show');
	}
})

// 切換頁面模式（明暗主題）
const switchMode = document.getElementById('switch-mode');

switchMode.addEventListener('change', function () {
	if (this.checked) {
		document.body.classList.add('dark');
	} else {
		document.body.classList.remove('dark');
	}
})

// LOGOUT
const logoutBtn = document.getElementById('logout');

logoutBtn.addEventListener('click', function () {
	window.location.href = '../index.html';
});
// DASHBOARD
const DASHBOARDBtn = document.getElementById('DASHBOARD');

DASHBOARDBtn.addEventListener('click', function () {
	window.location.href = 'index-帳號資訊.html';
});
// PAGE01
const PAGE01Btn = document.getElementById('PAGE01');

PAGE01Btn.addEventListener('click', function () {
	window.location.href = 'index-商品資訊.html';
});
// PAGE02
const PAGE02Btn = document.getElementById('PAGE02');

PAGE02Btn.addEventListener('click', function () {
	window.location.href = 'index-我的商品.html';
});
// PAGE03
const PAGE03Btn = document.getElementById('PAGE03');

PAGE03Btn.addEventListener('click', function () {
	window.location.href = 'index-用戶資訊.html';
});
// PAGE04
const PAGE04Btn = document.getElementById('PAGE04');

PAGE04Btn.addEventListener('click', function () {
	window.location.href = 'index-後台數據.html';
});
// PAGE05
const PAGE05Btn = document.getElementById('PAGE05');

PAGE05Btn.addEventListener('click', function () {
	window.location.href = 'index-匯款專區.html';
});
