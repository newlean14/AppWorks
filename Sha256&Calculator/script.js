/* ---------------SHA256 JS--------------- */

; (function ($, window, document, undefined) {
  // 在全局窗口對像上創建一個名為"method"的屬性，並將其初化為null
  window.method = null;

  // 將十六進製字符串轉換為字節數組的函數
  function hexToString(hex) {
    // 首先驗證hex是否為一個有效的十六進製字符串
    if (!hex.match(/^[0-9a-fA-F]+$/)) {
      throw new Error('is not a hex string.');
    }
    // 如果hex的長度是奇數，添加一個前導0以保證每兩個字符表示一個字節
    if (hex.length % 2 !== 0) {
      hex = '0' + hex;
    }
    // 將hex字符串轉換為字節數組
    var bytes = [];
    for (var n = 0; n < hex.length; n += 2) {
      var code = parseInt(hex.substr(n, 2), 16)
      bytes.push(code);
    }
    return bytes;
  }

  // 當文檔加載完成時執行的函數
  $(document).ready(function () {
    var input = $('#input');
    var output = $('#output');
    var checkbox = $('#auto-update');
    var dropzone = $('#droppable-zone');
    var option = $('[data-option]');
    var inputType = $('#input-type');
    // 定義一個執行函數，用於處理輸入和生成輸出
    var execute = function () {
      try {
        var type = 'text';
        var val = input.val();
        // 如果存在inputType元素，則獲取其值並設置type變量
        if (inputType.length) {
          type = inputType.val();
        }
        // 如果type為'hex'，將val轉換為字節數組
        if (type === 'hex') {
          val = hexToString(val);
        }
        // 調用"method"函數，並傳遞val和option的值作為參數，將結果設置為output的值
        output.val(method(val, option.val()));
      } catch (e) {
        output.val(e);
      }
    }
    // 自動更新函數，根據checkbox的狀態執行execute函數
    function autoUpdate() {
      if (!checkbox[0].checked) {
        return;
      }
      execute();
    }

    // 如果頁面上存在checkbox元素，則綁定事件處理程序
    if (checkbox.length > 0) {
      input.bind('input propertychange', autoUpdate);
      inputType.bind('input propertychange', autoUpdate);
      option.bind('input propertychange', autoUpdate);
      checkbox.click(autoUpdate);
    }

    // 如果頁面上存在dropzone元素，則處理文件拖放相關的操作
    if (dropzone.length > 0) {
      var dropzonetext = $('#droppable-zone-text');

      // 阻止默認的拖放行為
      $(document.body).bind('dragover drop', function (e) {
        e.preventDefault();
        return false;
      });

      // 檢測瀏覽器是否支持FileReader對象
      if (!window.FileReader) {
        dropzonetext.text('Your browser does not support.');
        $('input').attr('disabled', true);
        return;
      }

      // 當文件被拖動到dropzone時添加樣式
      dropzone.bind('dragover', function () {
        dropzone.addClass('hover');
      });

      // 當文件離開dropzone時移除樣式
      dropzone.bind('dragleave', function () {
        dropzone.removeClass('hover');
      });

      // 當文件被放置到dropzone時執行操作
      dropzone.bind('drop', function (e) {
        dropzone.removeClass('hover');
        file = e.originalEvent.dataTransfer.files[0];
        dropzonetext.text(file.name);
        autoUpdate();
      });

      // 當input元素的值發生改變時執行操作
      input.bind('change', function () {
        file = input[0].files[0];
        dropzonetext.text(file.name);
        autoUpdate();
      });

      var file;
      // 重新定義execute函數，用於處理文件的異步更新
      execute = function () {
        reader = new FileReader();
        var value = option.val();
        if (method.update) {
          var batch = 1024 * 1024 * 2;
          var start = 0;
          var total = file.size;
          var current = method;
          // 當文件讀取完成時執行的函數
          reader.onload = function (event) {
            try {
              // 調用current的update方法，並將結果設置為current變量
              current = current.update(event.target.result, value);
              asyncUpdate();
            } catch (e) {
              output.val(e);
            }
          };
          // 異步更新文件的函數
          var asyncUpdate = function () {
            if (start < total) {
              output.val('hashing...' + (start / total * 100).toFixed(2) + '%');
              var end = Math.min(start + batch, total);
              // 讀取文件的片段並調用reader.onload函數
              reader.readAsArrayBuffer(file.slice(start, end));
              start = end;
            } else {
              // 當文件更新完成時設置output的值
              output.val(current.hex());
            }
          };
          // 開始異步更新
          asyncUpdate();
        } else {
          // 如果不支持更新，則直接讀取整個文件並處理
          output.val('hashing...');
          reader.onload = function (event) {
            try {
              output.val(method(event.target.result, value));
            } catch (e) {
              output.val(e);
            }
          };
          reader.readAsArrayBuffer(file);
        }
      };
    }

    // 當按鈕被點擊時執行execute函數
    $('#execute').click(execute);

    // 根據URL中的路徑設置導航菜單中的活動鏈接樣式
    var parts = location.pathname.split('/');
    $('a[href="' + parts[parts.length - 1] + '"]').addClass('active');
  });
})(jQuery, window, document);