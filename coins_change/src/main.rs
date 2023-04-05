use std::{sync::Arc, io::stdin};

use cached::proc_macro::cached;

#[cached]
fn min_squares(squares: Arc<Vec<i32>>, val: i32) -> i32{
    if val == 0 {return 0;}

    let mut ans = i32::MAX;

    for c in squares.iter(){
        if *c <= val{
            let tmp = min_squares(Arc::clone(&squares), val-c);
            if tmp + 1 < ans{
                ans = tmp + 1
            }
        }
    }
    return ans
}


fn main() {
    let mut squares: Vec<i32> = Vec::new();
    
    let v: i32 = {
        let mut buffer = "".to_owned();
        stdin().read_line(&mut buffer).unwrap();
        buffer.trim().parse().unwrap()

    };

    let limit: i32 = (v as f32).sqrt() as i32 + 1; 
    
    for i in 1..limit{
        squares.push(i.pow(2));
    }

    let input = Arc::new(squares);


    println!("{}", min_squares(input, v))

}
