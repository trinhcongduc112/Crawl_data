---
title: Lock/Unlock routes in VRP
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
## Lock route cho mỗi lần khởi tạo

Nếu khởi tạo lộ trình lần đầu, người điều phối có thể chốt lộ trình bằng cách nhấn vào nút Lock Route màu xanh như hình dưới:

![1361](https://files.readme.io/e3d53eb-lock.png "lock.png")

Với các lần khởi tạo tiếp theo, nút Lock Route vẫn enable để người điều phối có thể chốt tiếp sau mỗi lần khởi tạo.

![1359](https://files.readme.io/24daeac-lock2.png "lock2.png")

* By default, after performing route optimization and locking route, the delivery tasks will be sent to the driver account on Mobile app. You will not be able to unlock route
* If for some reasons, you want to revoke the delivery task assigned to that driver, you can unlock the route by using the Unlock route configuration

## Activate Unlock route configuration

* Login with the top administrator account
* Navigate to **Organizations > Organization List** tab
* Click on **Edit** :fa-pencil: icon of the ***Branch*** which you want to activate the Unlock route configuration
* On the **Organization Information** screen, click on **Allow Unlock Route** check box
* Click **Save** to confirm the change

## Unlock route

* **Note** Before unlocking route, to ensure that none of the orders has been delivered, you should check the actual route by refreshing the Route optimization screen:
* Press **F5** on your keyboard
* Click on **Plan** text on the Timeline panel to switch to the Actual timeline panel
* View the delivery route. If a block of a specific delivery point has had an orange or green check mark :fa-check-circle: icon, that means orders for that delivery point have been delivered

<Image title="green yellow check in.png" alt={617} className="border" border={true} src="https://files.readme.io/1f1596d-green_yellow_check_in.png" />

* Switch back to the Plan timeline panel by clicking on **Actual** text
* Click on **Unlock** button, then click **OK** on the confirmation form
* The routes will have been successfully unlocked. Now you can optimize the routes again

- **Note**: The **Unlock** button will only unlock the most recent delivery shift. It will not unlock previously locked shifts
