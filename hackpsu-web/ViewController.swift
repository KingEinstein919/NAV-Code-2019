//
//  ViewController.swift
//  hackpsu-web
//
//  Created by Amey Deotale on 3/16/19.
//  Copyright © 2019 Amey Deotale. All rights reserved.
//

import UIKit
import WebKit

class ViewController: UIViewController {

    let baseURL : String = "http://162.243.169.143:5000/"
    var number : Int = 0
    var url : String = ""
    @IBOutlet weak var webUI: WKWebView!
    
    
    @IBAction func loadButton(_ sender: UIButton) {
        number = Int.random(in: 0 ... 3)
        url = baseURL+String(number)
        
        webUI.load(URLRequest(url: URL(string: url)!))
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }

    
}

