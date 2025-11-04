---
title: Intermodal Container Transport – Sea Model
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
  pages:
    - type: link
      title: Mobile app user interface
      url: >-
        https://docs.abivin.com/docs/freight-transport-sea-barge-mobile-app-interface#section-shipment-detail-screen
    - type: link
      title: Perform shipment tasks
      url: >-
        https://docs.abivin.com/docs/freight-transport-sea-barge-perform-shipment-tasks
---
The articles in this section will help the barge captains to navigate through the Mobile app and perform shipment tasks

> ❗️ Some notes about the Mobile app
>
> * The Mobile app for this model has only been developed for Android devices, not yet for iOS devices
> * The app interface is optimized for tablets. You might find it inconvenient to use the app on smartphones, due to the smaller screen sizes
> * ock:api-hea In order for the barge captain to be able to see and perform the assigned shipments, the IMEI or MAC Address of the tablet equipped for the barge must have been input in the barge database on Web app. Refer to this article for instruction: [**Manage Barges**](https://docs.abivin.com/docs/freight-transport-sea-barge-manage-barges#store-imeimac-address-of-the-barges-equipped-mobile-device)
> * If you use the MAC Address, you must set the MAC Address setting of the mobile device to **device MAC** instead of **randomized MAC**. See the below section to setup your device: [**Setup Mobile device with MAC Address**](https://docs.abivin.com/docs/freight-transport-sea-barge-mobile#setup-mobile-device-with-mac-address)

## Setup Mobile device with MAC Address

* If you wish to integrate the Mobile app with MAC Address, you must prepare a few things, details below:
* First, set the MAC Address setting of the barges' equipped mobile devices to use Device MAC Address. To do this, navigate to the WiFi setting section, select the Wifi network that the devices are currently connected to, then tap the gear icon :fa-gear: next to the network name. On the next screen there is a menu labeled **MAC Address Type**. Tap on that menu and select ***Use Phone/Device MAC***

<Image title="VEOlMp9UqF.png" alt={420} className="border" border={true} src="https://files.readme.io/9289460-VEOlMp9UqF.png" />

* Then, with the devices still connected to Wifi network, search the MAC Address of the device and inform to the Web dispatchers so that they can [store the MAC Address to the Barges' information](https://docs.abivin.com/docs/freight-transport-sea-barge-manage-barges#store-imeimac-address-of-the-barges-equipped-mobile-device) 

<Image title="ECO5Nx8RML.png" alt={408} className="border" border={true} src="https://files.readme.io/cea1138-ECO5Nx8RML.png" />

* After the dispatcher has stored the device's MAC Address to the Barge information, you need to log in to the Abivin vRoute Mobile app for the first time ***still using Wifi*** (Do not use 3G/4G). After the first successful login attempt, you can then freely use 3G/4G/ or Wifi
* **IMPORTANT NOTE** During your use, **DO NOT** clear the Abivin vRoute Mobile app cache because doing that will wipe out the MAC Address setting
* You can see the configuration process in the video below:

<Embed url="https://www.youtube.com/watch?v=W7ZN03_xoYI&list=PLZMWOfaNV00FQVPyiMPYa5MfbEVQl8KV6&index=5" title="MAC Address" favicon="https://www.youtube.com/s/desktop/a386e432/img/favicon.ico" image="https://i.ytimg.com/vi/W7ZN03_xoYI/hqdefault.jpg" provider="youtube.com" href="https://www.youtube.com/watch?v=W7ZN03_xoYI&list=PLZMWOfaNV00FQVPyiMPYa5MfbEVQl8KV6&index=5" html="%3Ciframe%20class%3D%22embedly-embed%22%20src%3D%22%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Fsrc%3Dhttps%253A%252F%252Fwww.youtube.com%252Fembed%252FW7ZN03_xoYI%253Flist%253DPLZMWOfaNV00FQVPyiMPYa5MfbEVQl8KV6%26display_name%3DYouTube%26url%3Dhttps%253A%252F%252Fwww.youtube.com%252Fwatch%253Fv%253DW7ZN03_xoYI%26image%3Dhttps%253A%252F%252Fi.ytimg.com%252Fvi%252FW7ZN03_xoYI%252Fhqdefault.jpg%26key%3Df2aa6fc3595946d0afc3d76cbbd25dc3%26type%3Dtext%252Fhtml%26schema%3Dyoutube%22%20width%3D%22854%22%20height%3D%22480%22%20scrolling%3D%22no%22%20title%3D%22YouTube%20embed%22%20frameborder%3D%220%22%20allow%3D%22autoplay%3B%20fullscreen%22%20allowfullscreen%3D%22true%22%3E%3C%2Fiframe%3E" />
