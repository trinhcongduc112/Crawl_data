---
title: Configuration Un(loading) Time
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
* A branch may manage several depots, so it is of great importance for a branch manager to use such configurations as Service Time at Branch, Dynamic Loading Time, Loading Time at Depot, Unloading Time at Customers in a flexible way. That is the purpose of the configuration **Un(loading) Time**. The only organization type that could enable this configuration is Branch.

* To enable this configuration, please follow these steps

* Step 1: Navigate to tab Organization, then select the branch that you want to enable this configuration from the organization list

* Step 2: Click the icon Pencil to the right side of the branch you want to enable this configuration. A form names Update Organization will pop up on the screen.

* Step 3:  In the form Update Organization, choose the tab More Configurations

* Step 4: In the left column of the tab More Configurations, select Un(loading) Time

<Image title="Branch - Unloading Time.png" alt={935} border={true} src="https://files.readme.io/9b44e37-Branch_-_Unloading_Time.png">
  Illustration (English)
</Image>

<Image title="Branch - Unloading Time (VIE).png" alt={934} border={true} src="https://files.readme.io/8b02f9a-Branch_-_Unloading_Time_VIE.png">
  Illustration (Vietnamese)
</Image>

You will see there are four checkboxes from top to bottom as follows

1. Use Services Time at Branch
2. Dynamic Loading Time
3. Enable Loading Time at Depot
4. Enable Unloading Time at Customer

* When you open the form, you could see that the box of Use Services Time at Branch is selected as default.  The base service time is also already filled. However, you can change this information based on your 

<Image title="Use Service Time (ENG).png" alt={932} border={true} src="https://files.readme.io/cecf8ac-Use_Service_Time_ENG.png">
  Illustration (English)
</Image>

<Image title="Use Service Time (VIE).png" alt={932} border={true} src="https://files.readme.io/be0fa62-Use_Service_Time_VIE.png">
  Illustration (Vietnamese)
</Image>

* If you check the box of **Dynamic Loading Time**, it means you choose to use this configuration for this branch and all of its depots. The other three boxes of **Use Services Time at Branch, Enable Loading Time at Depot, Enable Unloading Time at Customer** will be grayed out, which means the system disables these three configurations in this Branch and all of its depots.

<Image title="Dynamic Loading Time 9ENG).png" alt={934} border={true} src="https://files.readme.io/d6f547b-Dynamic_Loading_Time_9ENG.png">
  Illustration (English)
</Image>

<Image title="Dynamic Loading Time (VIE).png" alt={933} border={true} src="https://files.readme.io/5ac4cef-Dynamic_Loading_Time_VIE.png">
  Illustration (Vietnamese)
</Image>

* If you check the box of either **Enable Loading Time at Depot** or **Enable Unloading Time at Customer**, the line of Dynamic Loading Time will be grayed out and the entire configuration of Dynamic Loading Time will be disabled for this branch and all of its depots. However, the configuration of Use Services Time at Branch remains intact and the system still allows users to adjust time and loading unit in Service Time. To read more about this, click here **Service Time Calculation**(Loading Time at Depot)

<Image title="Uncheck 1.png" alt={934} border={true} src="https://files.readme.io/62d2b3b-Uncheck_1.png">
  Illustration (English)
</Image>

<Image title="Uncheck 2.png" alt={931} className="border" border={true} src="https://files.readme.io/38ea615-Uncheck_2.png" />

* If you check both two box of Enable Loading Time at Depot and Enable Unloading Time at Customer, the system will automatically uncheck the box of Dynamic Loading Time and Use Service Time at Branch. This means that the Loading Time is no longer subject to the timeframe set by the brand but to the timeframe at depots where delivery vehicles load goods and to the timeframe at the customers' delivery stop where the delivery man will unload the goods.

<Image title="Uncheck 4.png" alt={933} border={true} src="https://files.readme.io/c0fd74e-Uncheck_4.png">
  Illustration (English)
</Image>

<Image title="Uncheck 3.png" alt={931} border={true} src="https://files.readme.io/21005f6-Uncheck_3.png">
  Illustration (Vietnamese)
</Image>
