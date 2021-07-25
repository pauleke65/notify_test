import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/material.dart';

import 'package:firebase_messaging/firebase_messaging.dart';
import 'package:flutter_local_notifications/flutter_local_notifications.dart';

import 'notification_service.dart';

void main() {
  WidgetsFlutterBinding.ensureInitialized();
  NotificationService().init();
  runApp(MyApp());
}

class MyApp extends StatefulWidget {
  // This widget is the root of your application.
  @override
  _MyAppState createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  final Future<FirebaseApp> _initialization = Firebase.initializeApp();
  @override
  Widget build(BuildContext context) {
    return FutureBuilder(
        future: _initialization,
        builder: (context, snapshot) {
          if (snapshot.hasError) {
            return Center(
              child: Text("Error"),
            );
          }

          if (snapshot.connectionState == ConnectionState.done) {
            return MaterialApp(
              title: 'Flutter Demo',
              theme: ThemeData(
                // This is the theme of your application.
                //
                // Try running your application with "flutter run". You'll see the
                // application has a blue toolbar. Then, without quitting the app, try
                // changing the primarySwatch below to Colors.green and then invoke
                // "hot reload" (press "r" in the console where you ran "flutter run",
                // or simply save your changes to "hot reload" in a Flutter IDE).
                // Notice that the counter didn't reset back to zero; the application
                // is not restarted.
                primarySwatch: Colors.blue,
              ),
              home: MyHomePage(),
            );
          }

          return Center(child: CircularProgressIndicator.adaptive());
        });
  }
}

class MyHomePage extends StatefulWidget {
  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  final FirebaseMessaging _fcm = FirebaseMessaging.instance;

  void _getToken() async {
    String token = await _fcm.getToken(
        vapidKey:
            'BDP-5mwN-iDa8F4Rl4lAXo0MxzYqHH3riufJ1KWAp9ai9bHzzc9sd88I4FEK0Z7zUQJsAHKUHgwOeKliKlS2p4Y');
    print('Token is $token here');
  }

  @override
  void initState() {
    super.initState();
    FirebaseMessaging.onMessage.listen((RemoteMessage message) {
      print('Got a message whilst in the foreground!');
      print('Message data: ${message.data}');

      if (message.notification != null) {
        print('Message also contained a notification: ${message.notification}');

        showDialog(
            context: context,
            builder: (_) {
              return AlertDialog(
                  title: Text(message.notification.title),
                  content: Text(message.notification.body));
            });

        NotificationService().showNotification(message.notification);
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(),
      body: Center(
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            ElevatedButton(
              child: Text('I like puppies'),
              onPressed: () => _fcm.subscribeToTopic('puppies'),
            ),
            SizedBox(height: 20),
            ElevatedButton(
              child: Text('I hate puppies'),
              onPressed: () => _fcm.unsubscribeFromTopic('puppies'),
            ),
            SizedBox(height: 20),
            ElevatedButton(
              child: Text('Get Token'),
              onPressed: () => _getToken(),
            ),
          ],
        ),
      ),
    );
  }
}
