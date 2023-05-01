# DACN2_ComputerVision
DACN2_ComputerVision. xóa nền (nền trắng, đen, trong suốt), thay đổi nền, làm mờ nền, làm xám nền. API, website call api, desktop app call api.

Phần Mềm

  Pycharm
  
  visual studio code
  
	    plugin:     -python (chọn cái 78 triệu lượt tải), 
                        -Django(hình có chữ dj), 
                        -html css support, 
                        -html snippets, 
                        -html Boilerplate
		        -css Peek
		        -Color info
		        -Prettier (format code)
                        
  PtQT 5
  
  python --version (3.10.9)
  
  startUML
  
  
  


**Các Lỗi và hướng giải quyết**

          1.  D:\python\ThiGiacMayTinh\Project\venv\lib\site-packages\torchvision\models\_utils.py:208: UserWarning: The parameter 'pretrained' is deprecated since     0.13 and may be removed in the future, please use 'weights' instead.
            warnings.warn(
            D:\python\ThiGiacMayTinh\Project\venv\lib\site-packages\torchvision\models\_utils.py:223: UserWarning: Arguments other than a weight enum or `None` for 'weights' are deprecated since 0.13 and may be removed in the future. The current behavior is equivalent to passing `weights=DeepLabV3_ResNet101_Weights.COCO_WITH_VOC_LABELS_V1`. You can also use `weights=DeepLabV3_ResNet101_Weights.DEFAULT` to get the most up-to-date weights.
            warnings.warn(msg)

          hiển thị lỗi nhưng vẫn chạy ra kết quả thì dùng lệnh sau để không hiển thị lỗi nhưng vẫn ra kết quả
            import warnings
            warnings.filterwarnings("ignore", category=UserWarning) 


       ** 2. lỗi không cài / import được torch hoặc torchvision
          do phiên bản python lỗi
          https://www.youtube.com/watch?v=8DiYgiJ2VH8 
          => cài python phiên bản 3.10.9**

        - cài rembg để xóa nền ảnh
          pip install rembg 

      **  3. Lỗi torch.cuda.is_available()  ra FALSE
          https://stackoverflow.com/questions/60987997/why-torch-cuda-is-available-returns-false-even-after-installing-pytorch-with 
          => Cài đặt PyTorch mà không cần hỗ trợ CUDA (chỉ dành cho CPU)
          vào trang pytorch và chọn các tùy chọn để có lệnh cài torch, torchvision thích hợp**


        4. lỗi 'depth' is 6(CV_64F)
          chuyển các phép tính với file ảnh về unit8
            rgb_new = (rgb * 255).astype('uint8')

        5. plt.imshow()  => là ảnh đã chuển hóa (chia cho 255)
         => muốn dùng cv2.imwrite()  thì phải nhân ảnh lên 255 rồi chuyển bgr rồi lưu với unit8
          vd:
            rgb_new = (rgb * 255).astype('uint8')
                brg = cv2.cvtColor(rgb_new, cv2.COLOR_BGR2RGB)
                filename = os.path.splitext(os.path.basename(path))[0] + '_segmented.png'
                cv2.imwrite(os.path.join('./', filename), brg.astype('uint8'))


        ///LỖI trong dự án

        ufunc 'multiply' did not contain a loop with signature matching 
        types (dtype('<U1'), dtype('uint8')) -> None
            => là chưa ép kiểu biến gì đó (có thể là dữ liệu GET về là string nhưng 
              dùng int mới dc => phải ép kiểu)



        // LỖI trong api postman 

        1. Forbidden (CSRF cookie not set.): /blurBG_act
        [11/Apr/2023 21:38:38] "POST /blurBG_act HTTP/1.1" 403 2870

        là chưa gán dòng này trước hàm xử lý đó
        @api_view(['POST'])


        2. Could not send request
        Error: connect ECONNREFUSED 127.0.0.1:8000 lỗi ở postman
        => là bên vscode chưa load xong nên bên postman bị lỗi
