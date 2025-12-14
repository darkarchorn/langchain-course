
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()


def main():
    print("Hello from langchain-course!")
    information = """Elon Reeve Musk (sinh 28 tháng 6 năm 1971) là một doanh nhân, nổi tiếng với vai trò mấu chốt trong hai công ty Tesla, Inc. và SpaceX, cũng như chủ sở hữu của Twitter. Musk là người giàu nhất thế giới tính đến tháng 1 năm 2025; Forbes ước tính giá trị tài sản ròng của ông là vào khoảng 426 tỷ USD.

Musk sinh ra và lớn lên trong một gia đình giàu có ở Pretoria, Nam Phi, trước khi di cư đến Canada và nhập tịch nước này. Ông chuyển tới California vào năm 1995 để theo học Đại học Stanford. Tại đây, ông cùng người em trai Kimbal đồng sáng lập công ty phần mềm Zip2, sau được mua lại bởi Compaq vào năm 1999. Cùng năm đó, Musk đồng sáng lập X.com, một ngân hàng trực tiếp về sau sáp nhập thành PayPal. Năm 2002, Musk nhập tịch Mỹ, cùng thời điểm lúc eBay mua lại PayPal. Sử dụng số tiền thu được sau thương vụ, Musk thành lập công ty dịch vụ hàng không vũ trụ SpaceX vào năm 2002. Năm 2004, Musk đầu tư sớm vào công ty sản xuất xe điện Tesla, rồi thăng tiến và trở thành chủ tịch cũng như CEO của công ty này. Năm 2018, Ủy ban Giao dịch và Chứng khoán Hoa Kỳ (SEC) đâm đơn kiện Musk với cáo buộc rằng ông đã bịa đặt về việc đảm bảo được một khoản vay nhằm thâu tóm tư nhân Tesla, buộc Musk phải từ chức chủ tịch công ty và nộp một khoản tiền phạt. Năm 2022, ông mua lại Twitter, đổi tên nền tảng thành X vào năm sau. Tháng 1 năm 2025, Musk được cắt cử làm nhân viên đặc biệt của Bộ Hiệu quả Chính phủ trong nhiệm kỳ thứ hai của Tổng thống Hoa Kỳ Donald Trump.

Musk là nhà tài trợ lớn nhất trong cuộc tranh cử Tổng thống Hoa Kỳ 2024 và được đánh giá là người ủng hộ các đảng phái, nhà hoạt động có tư tưởng cực hữu. Đầu năm 2025, ông làm cố vấn cao cấp cho Tổng thống tân cử Donald Trump và trở thành chủ nhiệm trên danh nghĩa của DOGE. Sau một cuộc tranh cãi công khai trên mạng với Trump, Musk từ bỏ chính quyền Trump và tuyên bố sẽ thành lập đảng riêng mang tên Đảng Nước Mỹ.

Những hoạt động và quan điểm chính trị mà Musk bày tỏ đã tạo dựng hình ảnh của ông như một nhân vật gây phân cực. Ông đã bị chỉ trích vì nhiều phát ngôn phi khoa học và sai sự thật, bao gồm: lan truyền thông tin sai lệch về COVID-19, bình luận cổ súy phân biệt chủng tộc, miệt thị Semit và cộng đồng chuyển giới, cũng như rao giảng các thuyết âm mưu vô căn cứ. Việc ông mua lại Twitter đã dấy lên tranh cãi vì chính sách cắt giảm nhân sự khổng lồ, sự gia tăng phát ngôn gây thù ghét và sự lan truyền thông tin sai lệch trên nền tảng này. Vai trò của ông trong chính quyền nhiệm kỳ hai của Trump, cụ thể là cơ quan DOGE, đã phải hứng chịu phản ứng dữ dội từ dư luận Hoa Kỳ.

Tiểu sử
Elon Musk sinh vào sáng lúc 7 giờ 30 phút, ngày 28 tháng 6 năm 1971 tại Pretoria, Transvaal, Nam Phi.[2][3] Về việc đặt tên cho Elon, Maye và Errol định đặt theo tên của thành phố ở Pháp (Nice) nhưng Errol đồng ý đặt tên là Elon theo tên ông của Maye - J.Elon Haldeman, và Reve, tên thời con gái của bà ngoại Maye. Elon là con trai của bà Maye Musk (nhũ danh Haldeman) là một người mẫu và chuyên gia dinh dưỡng sinh ra tại Saskatchewan, Canada, lớn lên tại Nam Phi[4][5][6] và ông Errol Musk, một kỹ sư cơ điện, phi công và thủy thủ người Nam Phi.[7] Elon có một em trai là Kimbal (sinh năm 1972) và một em gái Tosca (sinh năm 1974).[11][6]

Ông ngoại là Tiến sĩ Joshua Haldeman có quốc tịch Canada nhưng sinh ra tại Mỹ.[12] Bà nội là người gốc Anh và cũng có tổ tiên là người nhập cư gốc Đức đầu tiên tại vùng đất Pennsylvania.[13][14] Sau khi cha mẹ ly hôn vào năm 1980, Elon chọn sống với cha ở ngoại ô thành phố Pretoria,[13] một lựa chọn mà Elon đưa ra hai năm sau khi bố mẹ ly thân nhưng sau đó cảm thấy hối hận.[15] Elon bị cha ghẻ lạnh, ông đã gọi cha mình là "một con người khủng khiếp".[15] Elon cũng có hai người anh em cùng cha khác mẹ.[16][17]

Từ nhỏ, Elon đã là một độc giả cuồng nhiệt[18] Vào năm 10 tuổi, ông đã có hứng thú với máy tính trong khi sử dụng Commodore VIC-20.[19] Elon đã học lập trình máy tính bằng cách sử dụng một hướng dẫn và đến năm 12 tuổi, đã bán mã nguồn của một video game dựa trên BASIC tạo ra Blastar cho tạp chí PC and Office Technology với giá khoảng 500 đô la.[20][21] Danh mục đọc của Elon gồm bộ sách Foundation của Isaac Asimov từ đó rút ra bài học rằng "bạn nên cố gắng thực hiện tập hợp các hành động có khả năng kéo dài nền văn minh, giảm thiểu xác suất của thời kỳ đen tối và giảm độ dài của thời kỳ đen tối nếu có".[15]

Thời đi học, ông chịu sự bắt nạt nghiêm trọng và đã từng phải nhập viện sau khi bị một nhóm bạn học ném xuống cầu thang.[15][18][22][23] Elon theo học trường dự bị Waterkloof House Preparatory School và trung học Bryanston High School[22] sau đó tốt nghiệp tại trường trung học Pretoria Boys High School.[23]

Mặc dù người cha nhất quyết muốn Elon vào học đại học tại Pretoria, nhưng Elon đã quyết tâm chuyển đến Hoa Kỳ, ông đã kể lại rằng "Tôi nhớ mình đã suy nghĩ và thấy rằng nước Mỹ là nơi có thể có những điều tuyệt vời hơn bất kỳ quốc gia nào trên thế giới."[24] Ông biết rằng việc đến Hoa Kỳ từ Canada sẽ dễ dàng hơn và chuyển đến đó trái với mong muốn của cha mình vào tháng 6 năm 1989, ngay trước sinh nhật thứ 18.[25][26] Sau khi có được hộ chiếu Canada thông qua bà Maye, người mẹ có gốc gác từ Canada.[27][28]

Học vấn
Trong thời gian đợi giấy tờ từ phía Canada, Elon theo học Đại học Pretoria khoảng 5 tháng.[29] Khi chuyển đến sống tại Canada, Musk ghi danh vào Đại học Queen tại Kingston năm 1989 để tránh phải gia nhập nghĩa vụ quân sự bắt buộc của Quân đội Nam Phi.[30]

Ông từ bỏ Đại học Queen năm 2000 để theo học ngành kinh tế và vật lý thuộc Đại học Pennsylvania; tốt nghiệp năm 1997 với bằng Cử nhân Kinh tế tại Trường Wharton thuộc Đại học Pennsylvania và bằng Cử nhân Khoa học Vật lý từ College of Arts and Sciences của Đại học Pennsylvania.[31][32][33][34][35]

Năm 1994, Musk đã tổ chức hai đợt thực tập tại Thung lũng Silicon vào mùa hè: tại một công ty khởi nghiệp lưu trữ năng lượng có tên là Pinnacle Research Institute, chuyên nghiên cứu các siêu âm điện phân để lưu trữ năng lượng và công ty khởi nghiệp Rocket Science Games tại Palo Alto.[36]

Bruce Leak, cựu kỹ sư trưởng đằng sau QuickTime của Apple, người đã thuê Musk, lưu ý: "Anh ta có năng lượng vô biên. Bọn trẻ ngày nay không biết gì về phần cứng hay cách thức hoạt động, nhưng anh ta có một nền tảng hacker PC và chỉ để tìm ra mọi thứ mà không sợ điều gì."[37]

Năm 1995, Musk được nhận vào chương trình tiến sĩ về vật lý năng lượng/khoa học vật liệu tại Đại học Stanford ở California.[38] Háo hức theo đuổi các cơ hội trong thời đại bùng nổ internet, tuy nhiên, thay vào đó, ông quyết định ra mắt công ty đầu tiên của mình, Zip2 Corporation.

Sự nghiệp kinh doanh
Zip2
Năm 1995, Musk khởi nghiệp với dự án Zip2, cung cấp phần mềm ấn hành nội dung số cho các tổ chức mới, cùng với em trai Kimbal Musk.[39] Errol Musk đã tài trợ cho họ 28,000 đô la đầu tiên.[40]

Năm 1999, bộ phận AltaVista của Compaq mua lại Zip2 với 307 triệu đô la tiền mặt và 34 triệu đô la cổ phiếu.[41]

PayPal
Musk đồng sáng lập X.com, một công ty về dịch vụ tài chính trực tuyến và thanh toán qua email tháng 3 năm 1999. Một năm sau đó, trong một cuộc sáp nhập 50/50 về vốn,[42] X.com mua lại Confinity,[43] một hãng vận hành một hệ thống thanh toán đấu giá có quy mô tương tự như X.com, gọi tên là Paypal. Musk đã sắp xếp thương vụ này do niềm tin vào việc chuyển khoản trực tiếp đang nở rộ của công nghệ P2P.[43] Musk tin rằng nhánh con Confinity sẽ trở thành phương tiện cần thiết để tích hợp và phát triển một nền tảng thanh toán giữa các cá nhân bên trong X.com.[43] Công ty kết hợp ban đầu thu nhận X.com làm tên tập đoàn, nhưng vào tháng 2 năm 2001, X.com đổi tên chính thức của nó thành Paypal Inc. Musk đã cổ vũ mạnh mẽ cho trọng tâm của một Paypal mới nhằm vào hệ thống thanh toán toàn cầu và rời khỏi những sự cung cấp tài chính lõi của X.com.[44]

Sự phát triển ban đầu của PayPal phần lớn là do một chiến dịch phát triển rộng khắp thành công của Musk.[45] Tháng 10 năm 2002, PayPal được eBay mua lại với giá 1.5 tỷ giá trị cổ phiếu.[46] Vào thời điểm bán, Musk, cổ đông lớn nhất của công ty, nắm 11.7% cổ phiếu của PayPal.[47]

SpaceX

Musk cùng Tổng thống Barack Obama tại bãi phóng Falcon 9 năm 2010
Musk thành lập công ty thứ ba của ông, Space Exploration Technologies (SpaceX), vào tháng 6 năm 2002[48] và hiện là CEO và Giám đốc Kỹ thuật của tập đoàn này. SpaceX phát triển và chế tạo các phương tiện phóng ra không gian với trọng tâm hướng vào việc phát triển công nghệ tên lửa. Hai tên lửa đầu tiên của công ty là Falcon 1 và Falcon 9 và phi thuyền đầu tiên của nó mang tên Dragon.[49]

SpaceX đã giành được hợp đồng 1,6 tỷ đô la với NASA ngày 23 tháng 12 năm 2008, cho 12 chuyến bay của Falcon 9 và Dragon vào Trạm Vũ trụ Quốc tế ISS, thay thế cho Space Shuttle của NASA sau khi nó hết thời gian hoạt động năm 2011. Ban đầu, Falcon 9/Dragon sẽ thay thế chức năng vận tải hàng hóa của Shuttle và việc vận chuyển phi hành gia sẽ được thực hiện bởi Tàu vũ trụ Soyuz. Tuy nhiên, SpaceX đã thiết kế Falcon 9/Dragon nhằm vào việc vận chuyển phi hành gia và Ủy ban Augustine (Cơ quan Hoa Kỳ phụ trách các chuyến bay có người lái vào vũ trụ) đã khuyến nghị việc vận tải hành khách bởi các công ty thương mại như SpaceX.[50]

Musk nói rằng ý tưởng về công nghệ vũ trụ của mình chịu ảnh hưởng từ series "Foundation" của Issac Asimov,[51] và xem việc khai phá vũ trụ như một bước quan trọng trong việc mở rộng—nếu không nói là bảo tồn-sự hiểu biết của đời sống con người.[52] Musk từng nói rằng sự sống trải trên nhiều hành tinh khác nhau có thể đóng vai trò như một hàng rào ngăn chặn những mối đe dọa sự tồn vong của loài người. "Một thiên thạch hay một siêu núi lửa có thể hủy diệt chúng ta, và chúng ta đối mặt với những thảm họa mà khủng long chưa từng biết tới: một virus được lập trình, một sự hình thành do sơ suất một vi lỗ đen, sự ấm lên toàn cầu thảm họa hoặc một công nghệ thậm chí chưa được biết đến nào đó có thể báo hiệu sự tiêu vong của chúng ta. Nhân loại đã tiến hóa hàng triệu năm, nhưng trong 60 năm gần đây các vũ khí nguyên tử tạo nên nguy cơ tiêu diệt chính chúng ta. Sớm hay muộn, chung ta phải mở rộng sự sống ra ngoài trái cầu xanh lam này-hoặc là tuyệt chủng." [53] Mục tiêu của Musk là giảm giá thành của một chuyến bay có chở người xuống còn 1/10 hiện nay.[54] Ông thành lập SpaceX với 100 triệu đô la từ tài sản ban đầu của mình. Ông hiện vẫn đóng vai trò điều hành lẫn chỉ đạo kĩ thuật của công ty đóng ở Hawthorne, California này.[55] Trong tiểu sử của Ashlee Vance, Musk tuyên bố rằng ông muốn thành lập một thuộc địa của loài người trên sao Hỏa vào năm 2040, với dân số khoảng 80.000 người.[19] Musk tuyên bố rằng, do bầu khí quyển của sao Hỏa thiếu oxy, nên tất cả các phương tiện giao thông trên sao Hỏa đều sẽ sử dụng động cơ điện (ô tô điện, tàu điện, Hyperloop, máy bay điện).[56] Musk tuyên bố vào tháng 6 năm 2016 rằng hai tàu đầu tiên của SpaceX sẽ hạ cánh xuống sao Hỏa vào năm 2022 mang theo các thiết bị cần thiết để xây dựng các trạm năng lượng và cơ sở hạ tầng hỗ trợ sự sống. Đến năm 2024, các phi hành gia của SpaceX sẽ chính thức đặt chân lên hành tinh Đỏ, mang theo tham vọng chinh phục sao Hỏa của nhân loại.[57] Trong một cuộc phỏng vấn với Axios năm 2018, Tỷ phú Elon Musk tuyên bố ông muốn là người đầu tiên đặt chân lên Sao Hỏa.

Trong 7 năm, SpaceX đã thiết kế dòng thiết bị phóng Falcon và phi thuyền đa mục đích Dragon từ chỗ không có gì. Tháng 9 năm 2009, tên lửa Falcon 1 trở thành phương tiện nhiên liệu lỏng đầu tiên do tư nhân hùn vốn đưa được một vệ tinh vào quỹ đạo Trái Đất. NASA đã chọn SpaceX để tham gia vào dự án đầu tiên tin cậy các công ty tư nhân vận chuyển hàng hóa tới ISS. Hợp đồng này, có giá trị từ 1.6 tỉ tới 3.1 tỷ đô la, là một dấu mốc quan trọng của trạm vũ trụ trong việc vận chuyển hàng tới trạm và trở lại. Bên cạnh những dịch vụ này, mục tiêu của SpaceX còn bao gồm việc đồng thời hạ giá các chuyến bay tới quỹ đạo và cải thiện độ tin cậy lên cỡ mười lần, trong khi tạo nên thiết bị phóng ra quỹ đạo đầu tiên có thể hoàn toàn tái sử dụng. Tuy hiện đang trong giai đoạn tìm cách đưa người ra ISS, năm 2011 Musk khẳng định mục đích cá nhân của ông là đưa người ra khai phá và định cư ở Sao Hỏa, trong khoảng 10-20 năm nữa.[58] Ngày 25 tháng 5 năm 2012, tàu SpaceX Dragon đáp xuống ISS, ghi dấu mốc lịch sử lần đầu tiên có một công ty tư nhân phóng và đáp thành công một phương tiên xuống Trạm Vũ trụ Quốc tế.[59]

Musk tin rằng chìa khóa để khiến việc du hành vũ trụ trở nên rẻ và hợp túi tiền hơn là phải làm cho tên lửa có khả năng tái sử dụng, mặc dù hầu hết các chuyên gia trong ngành vũ trụ đều không tin rằng tên lửa có khả năng tái sử dụng là một điều khả thi. Thứ hai ngày 21 tháng 12 năm 2015, SpaceX bắn một tên lửa vào không gian và hạ cánh nó trở về mặt đất, trong trạng thái hoàn toàn nguyên vẹn. Không chỉ tạo ra một bước ngoặt lịch sử trong việc chế tạo tên lửa tái sử dụng, thành công nói trên có sức ảnh hưởng rất lớn đến tương lai của ngành du lịch không gian.[60]

Vào ngày 6 tháng 2 năm 2018, SpaceX đã phóng thành công Falcon Heavy, tên lửa có công suất cao thứ tư từng được chế tạo (sau Saturn V, Energia và N1) đồng thời là tên lửa mạnh nhất hoạt động trong năm 2018.[61]

SpaceX là nhà sản xuất động cơ tên lửa tư nhân lớn nhất thế giới và hiện đang nắm giữ kỷ lục về tỷ lệ lực đẩy trên trọng lượng cao nhất cho động cơ tên lửa (Merlin 1D).[62][63] SpaceX đã sản xuất hơn 100 động cơ Merlin 1D và đưa vào hoạt động. Mỗi động cơ Merlin 1D có thể nâng được trọng lượng tương đương với 40 chiếc xe hơi gia đình theo chiều thẳng đứng. Kết hợp lại, 9 động cơ Merlin trong tên lửa Falcon 9 giai đoạn đầu tạo ra lực đẩy từ 5,8 đến 6,7 MN (1,3 đến 1,5 triệu pound), tùy thuộc vào độ cao.[64]

Vào cuối năm 2017, SpaceX đã tiết lộ thiết kế cho phương tiện phóng và hệ thống tàu vũ trụ thế hệ tiếp theo tên là Starship. SpaceX đang thiết kế chiếc tên lửa đặc biệt này với hai bộ phận có thể tái sử dụng là bộ phận phóng chính cao 187m và chiếc tàu vũ trụ cao 153m trên đỉnh. Sau khi chế tạo thành công, chiếc tên lửa BFR sẽ cao hơn tượng Nữ thần tự do khoảng 15%, có thể mang theo 100 phi hành gia và 150 tấn hàng hóa lên quỹ đạo Trái đất. Khi lên được quỹ đạo Trái đất, BFR có thể tiếp nhiên liệu trong không gian và tiếp tục hành trình tới Sao Hỏa trong 6 tháng. Tên lửa Starship sẽ là tên lửa lớn nhất và mạnh nhất lịch sử từ trước đến nay, du định BFR sẽ thay thế hoàn toàn Falcon 9, Falcon Heavy và Dragon trong những năm 2020 [cần dẫn nguồn].

Tesla Motors

Musk quan sát một bản mẫu lắp ráp trong sự kiện tái mở cửa nhà máy NUMMI, nay là Tesla Motors (Fremont, CA) năm 2010
Tesla Motors được Martin Eberhard và Marc Tarpening gây vốn vào tháng 7 năm 2003, Musk đầu tư thành lập tháng 2 năm 2004 và trở thành Chủ tịch Hội đồng Quản trị; nhưng đam mê của ông với ô tô điện đã có từ thời còn trẻ.[65] Do ảnh hưởng của khủng hoàng tài chính thế giới năm 2008 và kéo theo đó là một đợt cắt giảm nhân lực bắt buộc ở Tesla, Musk buộc phải đảm nhận thêm vị trí CEO.[66] Ông khẳng định đường hướng của công ty là đầu tiên phát triển những chiếc xe thể thao hạng sang để thu hút sự quan tâm tới xe điện và kiếm lợi nhuận ban đầu nhằm nuôi mục đích lâu dài là cung cấp ô tô điện phổ biến cho người bình dân, giảm đáng kể lượng tiêu thụ dầu thô toàn cầu.[67][68]

Musk đóng vai trò tích cực trong công ty và đặc biệt chỉ đạo thiết kế các mẫu sản phẩm cũng như định hướng chiến lược, nhưng dù là CEO ông không liên hệ sâu vào việc điều hành kinh doanh hàng ngày.[69] Ông được cho là nắm 32% cổ phần tại Tesla, tập đoàn này được định giá 13.9 tỷ đô la vào tháng 7 năm 2013[70][71]

Mẫu xe điện thể thao đầu tiên, Tesla Roadster 2008, với giá khởi điểm 109 nghìn đô la/chiếc bán được khoảng 2500 đơn vị tới 31 quốc gia, đồng thời bản thử nghiệm của nó nhận giải "Phát minh xuất sắc nhất" năm 2006 của tạp chí Time trong lĩnh vực "Phát minh về vận tải".[72][73] Tesla Model S, chiếc sedan xuất hiện trên thị trường tháng 6 năm 2012 đã trở thành hiện tượng của năm, đạt một loạt giải thưởng như giải Xe tiêu biểu nhất của năm 2013 của tạp chí Automobile.[74] Nó bán được 2650 chiếc trong năm 2012 ở Hoa Kỳ[72] và 4900 chiếc tại Bắc Mỹ chỉ trong quý I 2013, trở thành mẫu xe điện bán chạy nhất trong khu vực.[75] Model X, mẫu xe SUV-minivan, được giới thiệu tháng 9 năm 2012 và được bán ra năm 2015.[76]


Musk cùng với Thượng nghị sĩ bang California Dianne Feinstein một chiếc Tesla Model S (2010)
. Thế hệ thứ ba của xe điện Tesla là Model 3 ra mắt vào năm 2016.

Bên cạnh việc bán xe điện thương hiệu Tesla, Tesla Motors còn cung cấp động cơ điện cho Mercedes-Benz, Toyota và Musk dự tính sẽ cung cấp một mạng lưới các trạm sạc điện siêu nhanh cho ô tô trên khắp Bắc Mỹ trong năm 2013[77] Tháng 5 năm 2013, Tesla Motors cho thấy quý đầu tiên hoạt động có lợi nhuận kể từ khi nó niêm yết cổ phiếu năm 2011.[78]

Trong một cuộc phỏng vấn vào tháng 5 năm 2013 với All Things Digital, Musk nói rằng để khắc phục những hạn chế về phạm vi của ô tô điện, Tesla đang mở rộng mạng lưới các trạm tăng áp, tăng gấp ba số trên bờ Đông và Tây của Hoa Kỳ vào tháng 6, với kế hoạch nhiều hơn mở rộng trên khắp Bắc Mỹ, bao gồm Canada, trong suốt cả năm.[79] Tính đến ngày 29 tháng 1 năm 2016, Musk sở hữu khoảng 28,9 triệu cổ phiếu Tesla, tương đương với khoảng 22% cổ phần công ty.[80][81]

Vào năm 2014, Musk tuyên bố rằng Tesla sẽ cho phép các bằng sáng chế công nghệ của nó được sử dụng bởi bất kỳ ai có thiện chí trong nỗ lực lôi kéo các nhà sản xuất ô tô để tăng tốc độ phát triển của ô tô điện. "Thực tế không may là các chương trình xe điện (hoặc chương trình cho bất kỳ chiếc xe nào không đốt hydrocarbon) tại các nhà sản xuất lớn đều không tồn tại, chiếm trung bình ít hơn 1% tổng doanh số bán xe của họ", Musk nói [82]

Vào tháng 2 năm 2016, Musk tuyên bố rằng ông đã mua được tên miền Tesla.com từ Stu Grossman, người đã sở hữu nó từ năm 1992, và thay đổi trang chủ của Tesla thành tên miền đó.[83]

Ủy ban Chứng khoán và Sàn giao dịch Mỹ (SEC) đã chính thức khởi kiện Elon Musk vào tháng 9 năm 2018 vì hành vi gian lận và thao túng thị trường. Nguyên nhân là do CEO Elon Musk đã đăng trên trang Twitter cá nhân của mình, ý muốn mua lại toàn bộ Tesla và biến nó trở thành một công ty tư nhân.[84][85] Kết quả là, Musk và Tesla đã bị phạt 20 triệu đô la, và Musk buộc phải từ chức chủ tịch Tesla trong khi vẫn là CEO của Tesla.[86]

Vào tháng 1 năm 2019, Musk đã tới Trung Quốc để khởi công Tesla's Shanghai Gigafactory, đây là nhà máy quy mô lớn đầu tiên của công ty bên ngoài Hoa Kỳ. Một phần trong chuyến thăm Trung Quốc, Musk cũng đã gặp thủ tướng Trung Quốc Li Keqiang.[87] Trong quá trình trao đổi, Musk thú nhận tình yêu của ông dành cho Trung Quốc và mong muốn ông có thể đến thăm Trung Quốc thường xuyên hơn, thủ tướng Trung Quốc đã nói rằng "Chúng tôi có thể cấp cho ngài thẻ xanh của Trung Quốc nếu điều đó có ích." [88].

SolarCity
Elon Musk là người đề xuất ý tưởng ban đầu cho SolarCity, một công ty do hai người anh em họ của ông, Peter (COO) và Lyndon Rive (CEO), thành lập năm 2006.[89][90] Elon Musk hiện giữ chân Chủ tịch và là cổ đông lớn nhất của SolarCity, định hướng nó cùng với Tesla Motors như một phần trong chiến dịch chống lại sự ấm lên toàn cầu.[91] Sau vài năm phát triển, SolarCity, chủ yếu hoạt động ở California, đã vươn lên thành nhà cung cấp năng lượng mặt trời cho dân cư lớn nhất Hoa Kỳ từ năm 2011.[92] SolarCity cũng bước chân vào lĩnh vực ô tô điện từ năm 2009,[93] và hợp tác với Tesla Motors nhằm kết hợp giữa pin điện ô tô với pin mặt trời, cung cấp các trạm sạc miễn phí cho xe điện hiệu Tesla và phương tiện lưu trữ điện mặt trời trong những thời điểm công suất hoạt động thấp.[94][95] SolarCity cũng tham gia các chương trình từ thiện, đầu tư các dự án hợp tác với chính phủ, quân đội, và các công ty khác như Google Inc. với Google Fund.[96] Lyndon Rive kể rằng Elon Musk chỉ có rất ít thời gian cho SolarCity, chỉ liên lạc qua điện thoại vài giờ mỗi tháng và họp hội đồng quản trị, nhưng vẫn bao quát toàn bộ hoạt động của công ty.[95]

Neuralink
Musk standing next to bulky medical equipment on a stage
Musk thảo luận về thiết bị của Neuralink trong trình diễn vào năm 2020
Năm 2016, Musk đồng sáng lập Neuralink, một công ty khởi nghiệp về công nghệ thần kinh, với khoản đầu tư 100 triệu USD.[97][98] Neuralink nhằm mục đích tích hợp bộ não con người với trí tuệ nhân tạo (AI) bằng cách tạo ra các thiết bị nhúng trong não để tạo điều kiện hợp nhất con người với máy móc. Công nghệ như vậy cho phép tăng cường bộ nhớ hoặc cho phép thiết bị cấy ghép trên con người giao tiếp với phần mềm.[99][100] Công ty cũng hy vọng sẽ phát triển các thiết bị điều trị các tình trạng thần kinh như bệnh Alzheimer, chứng mất trí nhớ và chấn thương tủy sống.[101]

Vào năm 2019, Musk công bố nghiên cứu về một thiết bị giống như máy may có thể nhúng các sợi chỉ vào não người. Musk được liệt kê như là tác giả duy nhất của bài báo khoa học đăng tháng 10 năm 2019 nêu chi tiết một số nghiên cứu của Neuralink, mặc dù việc Musk được liệt kê như vậy đã khiến các nhà nghiên cứu của nhóm Neuralink không được xếp hạng. Tại một cuộc trình diễn trực tiếp vào năm 2020, Musk đã mô tả một trong những thiết bị đầu tiên của họ là "Fitbit trong hộp sọ của bạn" có thể sớm chữa khỏi bệnh tê liệt, điếc, mù và các khuyết tật khác. Nhiều nhà khoa học thần kinh và ấn phẩm đã chỉ trích những tuyên bố này.[102][103][104] MIT Technology Review mô tả chúng là "có tính suy đoán cao" và là "nhà hát khoa học thần kinh".[102] Trong cuộc trình diễn, Musk đã tiết lộ một con lợn được cấy ghép thiết bị của Neuralink để theo dõi hoạt động thần kinh liên quan đến mùi. Năm 2022, Neuralink thông báo các thử nghiệm lâm sàng sẽ bắt đầu tiến hành vào cuối năm.[105]

Neuralink đã tiến hành thử nghiệm động vật trên khỉ macaque tại Đại học California, Trung tâm nghiên cứu linh trưởng của Davis. Vào năm 2021, công ty đã phát hành một video trong đó một con Macaque chơi trò chơi điện tử Pong thông qua bộ cấy ghép Neuralink. Các cuộc thử nghiệm trên động vật của công ty, gây ra cái chết của một số con khỉ, đã dẫn đến những cáo buộc về sự tàn ác với động vật. Ủy ban Bác sĩ về Y học có Trách nhiệm đã cáo buộc rằng các thử nghiệm trên động vật của Neuralink đã vi phạm Đạo luật Phúc lợi Động vật. Các nhân viên đã phàn nàn rằng áp lực từ Musk để đẩy nhanh quá trình phát triển đã dẫn đến các thí nghiệm bị hỏng và cái chết của động vật không cần thiết.[106] Vào năm 2022, một cuộc điều tra liên bang đã được tiến hành đối với các vi phạm phúc lợi động vật có thể có của Neuralink.[107]

Công ty Boring
Năm 2017, Musk thành lập Công ty Boring, công ty xây dựng đường hầm dưới lòng đất cho các phương tiện chuyên dụng, công suất lớn có thể di chuyển với tốc độ 150 dặm một giờ (240 km/h) và do đó vượt qua giao thông trên mặt đất ở các thành phố lớn.[108][109] Đầu năm 2017, công ty bắt đầu thảo luận với các cơ quan quản lý và bắt đầu xây dựng một "rãnh thử nghiệm" rộng 30 ft (9,1 m), dài 50 ft (15 m) và sâu 15 ft (4,6 m) tại cơ sở văn phòng của SpaceX, vì điều đó không cần giấy phép. Đường hầm Los Angeles, có chiều dài chưa đến 3,2 km, ra mắt các nhà báo vào năm 2018.[110] Đường hầm này được sử dụng cho Tesla Model X và được cho là khá khó khăn khi di chuyển ở tốc độ dưới mức tối ưu.[111]

Hai dự án đường hầm được công bố vào năm 2018, ở Chicago và Tây Los Angeles, đã bị hủy bỏ.[112][113] Tuy nhiên, một đường hầm bên dưới Trung tâm Hội nghị Las Vegas đã được hoàn thành vào đầu năm 2021.[114] Các quan chức địa phương cũng đã phê duyệt việc mở rộng thêm hệ thống đường hầm.[115] Vào năm 2021, việc xây dựng đường hầm cho Fort Lauderdale, Florida đã được phê duyệt.[116]

Twitter
Đầu năm 2017, Musk bày bắt đầu tỏ sự quan tâm đến việc mua Twitter,[117] trước đó ông đã đặt câu hỏi về cam kết của nền tảng này đối với quyền tự do ngôn luận.[118][119] Vào tháng 1 năm 2022, Musk bắt đầu mua cổ phiếu Twitter và đạt 9,2% cổ phần vào tháng 4 năm 2022,[120] khiến ông trở thành cổ đông lớn nhất của Twitter tại thời điểm đó.[121] Khi sự việc này được tiết lộ công khai, cổ phiếu Twitter đã trải qua đợt tăng giá trong ngày lớn nhất kể từ khi công ty IPO năm 2013.[122] Vào ngày 4 tháng 4 năm 2022, Musk đã đồng ý với một thỏa thuận bổ nhiệm ông vào ban giám đốc của Twitter và đồng thời cấm ông mua hơn 14,9% cổ phần của công ty.[123][124] Tuy nhiên, vào ngày 13 tháng 4, Musk đã đưa ra lời đề nghị trị giá 43 tỷ đô la để mua lại Twitter, khởi động một cuộc mua thâu tóm để mua lại 100% cổ phiếu của Twitter với giá 54,20 đô la một cổ phiếu.[121][125] Đáp lại, hội đồng quản trị của Twitter đã thông qua một kế hoạch "viên thuốc độc" đáp ứng quyền cổ đông để làm cho bất kỳ nhà đầu tư đơn lẻ nào sở hữu hơn 15% cổ phần của công ty mà không có sự chấp thuận của hội đồng quản trị sẽ tốn kém hơn.[126] Tuy nhiên, vào cuối tháng 4 năm 2020, Musk đã kết thúc thành công cuộc đấu thầu của mình với giá khoảng 44 tỷ đô la.[127] Số tiền này bao gồm khoản vay khoảng 12,5 tỷ đô la thế chấp bằng cổ phiếu Tesla của ông và 21 tỷ đô la tài trợ vốn cổ phần.[128][129] Vào tháng 7 năm 2023, Musk thông báo rằng Twitter sẽ đổi tên thành X và logo con chim sẽ không còn được sử dụng nữa.[130][131]

Hoạt động khác
Musk từng có kế hoạch cho một dự án mang tên "Ốc đảo Sao Hỏa" vào năm 2001 nhằm mục đích đưa một nhà kính thu nhỏ thử nghiệm lên Sao Hỏa, mang nhiều loại rau củ để trồng trên đất sao Hỏa.[132] Dự án này bị Musk dừng lại do ông sau đó đi tới kết luận rằng vấn đề cơ bản ngăn cản con người có thể trở thành một nền văn minh sinh sống ngoài không gian thực sự là việc thiếu một tiến bộ bước ngoặt trong công nghệ tên lửa; đó chính là thời điểm ông tập trung hoàn toàn vào dự án SpaceX.

Mục tiêu dài hạn của Musk là thông qua SpaceX đưa loài người phát triển thành một nền văn minh ngoài không gian thực thụ.[133] Cụ thể, ông định đưa được nhìn thấy trong đời mình, một thuộc địa với 80.000 người được thành lập trên Sao Hỏa. Ông hy vọng sẽ trên hành tinh đỏ, nói rằng: "Hẳn sẽ khá thú vị để chết trên Sao Hỏa..."[51]

Musk từng tham gia ủng hộ Ủy ban Hành động Chính trị Hoa Kỳ FWD.us, một tổ chức vận động nghị trường cho cải cách chính sách nhập cư do các doanh nhân ở Thung lũng Silicon đại diện bởi Mark Zuckerberg gây dựng. Tuy nhiên tháng 5 năm 2013, Musk công khai rút bỏ sự ủng hộ khi FWD.us đưa ra quảng cáo cho một dự án vận chuyển dầu thô đi ngược lại lý tưởng bảo vệ môi trường của ông. Cùng với một số thành viên khác như David Sacks, ông rút khỏi tổ chức và phê phán chính sách của tổ chức vận động hành lang thường ủng hộ cả hai chiều hướng chính trị cùng lúc để kiếm sự hậu thuẫn từ giới lập pháp, gọi điều đó là "vô đạo đức":[134] "Bạn phải chiến đấu trên lẽ phải của mục đích, chứ không phải chơi một trò Machiavelli mà bạn đồng ý ủng hộ những thứ xấu xa để những thứ tốt đẹp được thông qua".[51]

Tháng 7 năm 2012, Musk thông báo về một dự án hoàn toàn mới của ông mang tên "Hyperloop", một hệ thống đường hầm phản lực chạy bằng năng lượng mặt trời, được ông kì vọng là sẽ cho phép di chuyển từ San Francisco đến Los Angeles trong vòng ít nhất 30 phút (nghĩa là gần đạt tới tốc độ âm thanh).[135] Elon Musk dự trù dự án này tiêu tốn khoảng 6 tỷ đô la, tức chỉ bằng một phần 10 chi phí xây dựng đường tàu cao tốc; các chi tiết thiết kế của Hyperloop được Musk công bố vào tháng 8 năm 2013.[136]

OpenAI và xAI
Năm 2015, Musk đồng sáng lập OpenAI, một công ty nghiên cứu trí tuệ nhân tạo (AI) phi lợi nhuận nhằm phát triển trí tuệ nhân tạo chung nhằm mục đích an toàn và có lợi cho nhân loại.[137]

Năm 2018, Musk rời hội đồng quản trị OpenAI để tránh những xung đột có thể xảy ra trong tương lai với vai trò Giám đốc điều hành của Tesla khi công ty sau này ngày càng tham gia nhiều hơn vào AI thông qua Tesla Autopilot.[138]

Vào ngày 12 tháng 7 năm 2023, Elon Musk đã ra mắt một công ty trí tuệ nhân tạo có tên là xAI, nhằm mục đích phát triển một chương trình AI tạo ra để cạnh tranh với các dịch vụ hiện có như ChatGPT.[139] Công ty đã thuê các kỹ sư từ Google và OpenAI. Musk đã nhận được tài trợ từ các nhà đầu tư vào SpaceX và Tesla.[140]

Thành tựu
Những thành tựu đạt được đã đưa Elon Musk lên vị trí một trong những doanh nhân có nhiều ảnh hưởng nhất trên thế giới cũng như một biểu tượng của ngành công nghệ không gian. Ông xuất hiện trong danh sách 100 nhân vật quan trọng nhất thế giới năm 2010 của tạp chí Time,[141] danh sách 75 nhân vật ảnh hưởng nhất thế kỷ XXI của tạp chí Esquire,[52] danh sách 20 CEO quyền lực nhất Hoa Kỳ dưới 40 tuổi của Forbes.[142], danh hiệu Nhà cách tân của năm (2007) của tạp chí R&D Magazine,[143] Doanh nhân của năm (2007) của tạp chí Inc Magazine,[144] xếp vào những Huyền thoại sống hàng không năm 2010 bởi Quỹ Kitty Hawk (2010),[145] Doanh nhân ô tô của năm (2010).[146]

Ông cũng nhận các giải thưởng như Huy chương Vàng của Hội Hoàng gia Hàng không học Anh (2012),[147] Huy chương Vàng Không gian của Liên đoàn Hàng không Quốc tế (FAI) năm 2010,[148] Giải thưởng Heinlein cho Tiến bố trong Thương mại hóa Không gian năm 2011,[149] Giải thưởng George Low của Viện Hàng không và Hàng không vũ trụ Hoa Kỳ,[150] Cúp Von Braun của Hội Không gian Quốc gia.[151]

Ông nhận bằng tiến sĩ danh dự ngành thiết kế từ Cao đẳng Thiết kế Trung tâm[152] và bằng tiến sĩ danh dự ngành kĩ thuật hàng không từ Đại học Surrey.[153]

Vào tháng 6 năm 2016, Business Insider đã đưa Musk vào danh sách "10 nhà kinh doanh nhìn xa trông rộng hàng đầu tạo ra giá trị cho thế giới" cùng với Mark Zuckerberg và Sal Khan.[154]

Vào tháng 12 năm 2016, Musk xếp hạng thứ 21 trong danh sách Những người quyền lực nhất thế giới của Forbes.[155]

Đạo diễn bộ phim Iron Man kể lại rằng Elon Musk chính là nhân vật đã gây cảm hứng để xây dựng nhân vật Tony Stark trong bộ phim ăn khách nói trên.[141] Bản thân Elon cũng được ví như một Iron Man ngoài đời thực và ông có tham gia một cảnh (đóng vai chính mình)[156] trong Iron Man 2 với tư cách diễn viên khách mời (cameo), trong khi nhà máy của SpaceX là một địa điểm quay phim nói trên.[157] Chiếc máy bay Dassault Falcon 900 model 1994 của ông được dùng trong bộ phim "Thank You for Smoking" (2005) mà ông có đóng một vai cameo là phi công[158][159]

Vào tháng 12 năm 2021, tạp chí Time đã vinh danh Elon Musk là "Nhân vật của năm".[160]

Vào ngày 20 tháng 5 năm 2022, Musk đã được chính phủ Brazil trao tặng Huân chương Quốc phòng sau khi đàm phán triển khai dịch vụ internet Starlink tại rừng nhiệt đới Amazon.[161]

Hoạt động cá nhân
Từ thiện
Musk là chủ tịch của Quỹ Musk, tuyên bố mục đích chính là cung cấp các hệ thống năng lượng mặt trời trong các khu vực thảm họa cũng như các mục tiêu khác.[162][163] Vào năm 2010, Quỹ Musk hợp tác với SolarCity để tặng một hệ thống năng lượng mặt trời 25 kW cho trung tâm ứng phó với cơn bão của Liên minh Cộng đồng South Bay ở Coden, Alabama.[164] Vào tháng 7 năm 2011, Quỹ Musk đã quyên góp 250,000 đô la Mỹ đối với một dự án năng lượng mặt trời ở Sōma, Fukushima, Nhật Bản, một thành phố đã bị tàn phá nặng nề bởi sóng thần.[165]

Vào tháng 7 năm 2014, Musk được họa sĩ truyện tranh Matthew Inman và William Terbo, cháu của Nikola Tesla ngỏ lời về việc quyên góp 8 triệu đô la Mỹ hướng tới việc xây dựng Trung tâm khoa học Tesla tại Wardenclyffe.[166] Cuối cùng, Musk đã đồng ý quyên góp 1 triệu đô la Mỹ đối với dự án và cũng cam kết xây dựng một máy siêu tăng áp Tesla trong bãi đậu xe của bảo tàng.[167]

Vào tháng 1 năm 2015, Musk đã quyên góp 10 triệu đô la Mỹ cho viện nghiên cứu Future of Life Institute để điều hành một chương trình nghiên cứu toàn cầu nhằm giữ trí tuệ nhân tạo có lợi cho nhân loại.[168][169][170]

Vào tháng 10 năm 2018, trong nỗ lực giúp giải quyết Khủng hoảng nước Flint, tỷ phú Elon Musk và Quỹ Musk đã quyên góp hơn 480.000 đô la để lắp đặt các đài phun nước mới với hệ thống lọc để tiếp cận với nước sạch tại tất cả các trường thuộc Flint, Michigan.[171] Tính đến năm 2019, khoảng 30.000 trẻ em ở tất cả 12 trường trong khu vực có nước uống miễn phí, an toàn từ các hệ thống lọc nước.[172]

Elon Musk là một nhà tài trợ hàng đầu cho ACLU.[173]

Vào tháng 10 năm 2019, Elon Musk đã quyên góp 1 triệu đô la Mỹ cho Team Trees là một phong trào gây quỹ với mục tiêu trồng được 20 triệu cây trước năm 2020. [note 1] và phối hợp với Tổ chức Arbor Day là một tổ chức giáo dục và bảo tồn phi lợi nhuận được thành lập vào năm 1972 tại Nebraska, Hoa Kỳ bởi John Rosenow. Đây là tổ chức phi lợi nhuận lớn nhất dành riêng cho việc trồng cây.[174][175][176]

Gia đình
Tosca Musk là em gái của Elon, là một nhà làm phim. Cô là người sáng lập của Musk Entertainment và đã sản xuất nhiều bộ phim khác nhau.[177]

Musk đã gặp người vợ đầu tiên của mình, nhà văn người Canada Justine Wilson, trong khi cả hai đều là sinh viên tại Đại học Queen ở Ontario, Canada. Họ kết hôn năm 2000 và ly thân năm 2008.[178] Con trai đầu của họ, Nevada Alexander Musk, mất vì hội chứng đột tử ở trẻ sơ sinh (SIDS) khi được 10 tuần tuổi.[179] Sau đó họ có năm người con trai thông qua thụ tinh trong ống nghiệm[180]- gồm một cặp song sinh vào năm 2004 (Griffin và Xavier), tiếp theo là sinh ba năm 2006 (Kai, Saxon và Damian). Họ chia sẻ quyền nuôi cả năm người con trai.[181]

Năm 2008, Elon Musk bắt đầu hẹn hò với nữ diễn viên người Anh Talulah Riley và kết hôn năm 2010. Tháng 1 năm 2012, Musk tuyên bố rằng ông đã chấm dứt mối quan hệ bốn năm[10][182] với Riley thông qua trang Twitter cá nhân, "Đó là một bốn năm tuyệt vời. Tôi sẽ yêu em mãi mãi. Em sẽ làm cho ai đó rất hạnh phúc vào một ngày nào đó."[183]

Tháng 7 năm 2013, Elon Musk và Riley tái hợp. Tháng 12 năm 2014, Musk đệ đơn ly hôn lần thứ hai với Riley; tuy nhiên sau đó đã rút đơn.[184] Tháng 3 năm 2016, các phương tiện truyền thông tiết lộ thủ tục ly hôn một lần nữa đang được tiến hành, lần này là từ phía Riley muốn ly hôn Elon Musk.[185] Vụ ly hôn được hoàn tất vào cuối năm 2016.[186]

Musk bắt đầu hẹn hò với nữ diễn viên người Mỹ Amber Heard vào năm 2016, họ chia tay sau một năm do lịch trình vướng mắc.[187][188]

Vào ngày 7 tháng 5 năm 2018, Elon Musk và nữ nghệ sĩ người Canada, Grimes tiết lộ rằng họ đã bắt đầu hẹn hò.[189][190][191]

Vào ngày 8 tháng 1 năm 2020, Grimes tuyên bố rằng cô đang mang thai đứa con đầu lòng của họ.[192][193] Con trai của Grimes và Musk chào đời vào ngày 4 tháng 5 năm 2020.[194][195] Theo Elon Musk và Grimes, tên em bé là "X Æ A-12" (được phát âm là "Ex Ash A Twelve"[196] hoặc "Ex Aye Eye"[197]), tuy nhiên tên này được coi là không hợp lệ theo luật California, bởi vì nó chứa các ký tự không có trong bảng chữ cái hiện tại bảng chữ cái tiếng Anh,[198] và sau đó được đổi thành "X Æ A-Xii", điều này đã gây ra sự nhầm lẫn, vì "Æ" vẫn chưa có trong bảng chữ cái tiếng Anh hiện đại.[199] Musk xác nhận rằng mình đã tạm chia tay bạn gái vào tháng 9 năm 2021.[200][201]

Tham gia chương trình Joe Rogan
Vào ngày 6 tháng 9 năm 2018, Musk xuất hiện trên chương trình podcast The Joe Rogan Experience cùng thảo luận về nhiều chủ đề khác nhau trong hơn hai giờ. Trong vòng năm ngày, sự có mặt của Elon đã thu hút được 10 triệu lượt xem trên kênh YouTube của chương trình này.[202]

Một trong những hành động gây tranh cãi của chương trình là việc Elon Musk hút một điếu xì gà, Rogan xác nhận đó là cần sa được cuốn bởi giấy xì gà. Đáp lại câu hỏi của Rogan về tần suất hút cần sa, Musk trả lời:

“	
"Hầu như không bao giờ. Tôi biết nhiều người thích cần sa và họ thấy vậy là tốt, nhưng tôi không thấy điều đó tốt lắm cho năng suất và... nó không dành cho tôi".

”
Tờ The Washington Post nhận định: "Trong giới truyền thông, nó đã trở thành một câu chuyện về sự bất ổn ngày càng tăng của Musk ..."[203] Giá trị cổ phiếu của Tesla đã giảm sau vụ việc, trùng hợp với xác nhận về sự ra đi của Phó chủ tịch tài chính toàn cầu Tesla Justin McAnear đầu ngày hôm đó.[204] Tạp chí Fortune tự hỏi nếu sử dụng cần sa có thể diễn ra sự phân chia hợp đồng cho SpaceX với Không quân Hoa Kỳ, mặc dù một phát ngôn viên của USAF đã nói với The Verge rằng không có cuộc điều tra nào được thực hiện và Không quân vẫn đang xử lý tình huống.[205][206]

Trong một cuộc phỏng vấn trên 60 Minutes, Elon nói về vụ việc hút cần sa:

“	
"Tôi không hút pot (pot là một loại chất gây nghiện thường là cần sa hoặc cỏ Mỹ nên về cơ bản vẫn là sử dụng chất gây nghiện). Như bất cứ ai đã xem podcast đó có thể thấy, tôi không biết cách hút pot."[207]
    
"""
    summary_template = """
    Given the information {information} about a person I want you to create: 1. A short summary 2. Two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )
    llm = ChatOpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio"
    )
    chain = summary_prompt_template | llm
    response = chain.stream(input={"information": information})
    for chunk in response:
        if chunk.content:
            print(chunk.content, end="", flush=True)

if __name__ == "__main__":
    main()
