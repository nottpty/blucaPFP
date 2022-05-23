from PIL import Image
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def loop_create_images(assets):
    # ----------- Setup loop ---------- #
    # assets = ["background", "head2", "costume", "face", "head", "weapon"]
    # max_amount_per_asset = [3, 3, 3, 3, 3, 3]
    # min_amount_per_asset = [0, 0, 0, 0, 0, 0]
    # runner_main_index = 0

    counter = 1
    background = assets[0]
    head2 = assets[1]
    costume = assets[2]
    face = assets[3]
    head = assets[4]
    weapon = assets[5]
    for selection_asset in background:
        for i in head2:
            for j in costume:
                for k in face:
                    for l in head:
                        for m in weapon:
                            print_image(str(selection_asset), str(i), str(j), str(k), str(l), str(m), str(counter))
                            counter = counter + 1
                            if counter == 100:
                                break
                    if counter == 100:
                        break
                if counter == 100:
                    break
            if counter == 100:
                break
        if counter == 100:
            break
    print(f'End processing with ' + str(counter) + ' images')


    # for _ in range(assets):
    #     for main_asset in range(max_amount_per_asset):
    #         for sub_asset in range(main_asset[main_asset]):
    #             print_image(i)

def print_image(num_background, num_head2, num_costume, num_face, num_head, num_weapon, current_number):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Start processing for number '+current_number)  # Press ⌘F8 to toggle the breakpoint.

    # # Open image using Image module
    # im = Image.open("images/Summoning_lab.jpg")
    # # Show actual Image
    # im.show()
    # # Show rotated Image
    # im = im.rotate(45)
    # im.show()

    # ----------- Pre-setup images ---------- #

    # Back Image - layer 0
    background_img_location_0 = 'images/background/background_'+num_background+'.png'

    # Head Image - layer 1
    head2_img_location_1 = 'images/head2/head2_'+num_head2+'.png'

    # Costume Image - layer 2
    costume_img_location_2 = 'images/costume/costume_'+num_costume+'.png'

    # Face Image - layer 3
    face_img_location_3 = 'images/face/face_'+num_face+'.png'

    # Head Image - layer 4
    head1_img_location_4 = 'images/head/head1_'+num_head+'.png'

    # Weapon Image - layer 5
    weapon_img_location_5 = 'images/weapon/weapon_'+num_weapon+'.png'

    # ----------- Open images ---------- #

    # Open Background Image
    background_img_0 = Image.open(background_img_location_0)

    # Open Head 2 Image
    head2_img_1 = Image.open(head2_img_location_1)

    # Open Front Image
    costume_img_2 = Image.open(costume_img_location_2)

    # Open Face Image
    face_img_3 = Image.open(face_img_location_3)

    # Open Head Image
    head_img_4 = Image.open(head1_img_location_4)

    # Open Weapon Image
    weapon_img_5 = Image.open(weapon_img_location_5)

    # ----------- Convert images to color code ---------- #![](images/head2.png)

    # Convert image to RGBA
    background_img_0 = background_img_0.convert("RGBA")
    head2_img_1 = head2_img_1.convert("RGBA")
    costume_img_2 = costume_img_2.convert("RGBA")
    face_img_3 = face_img_3.convert("RGBA")
    head_img_4 = head_img_4.convert("RGBA")
    weapon_img_5 = weapon_img_5.convert("RGBA")

    # ----------- Paste an image to base image ---------- #

    # Paste the frontImage at (width, height)
    background_img_0.paste(head2_img_1, None, head2_img_1)
    background_img_0.paste(costume_img_2, None, costume_img_2)
    background_img_0.paste(face_img_3, None, face_img_3)
    background_img_0.paste(head_img_4, None, head_img_4)
    background_img_0.paste(weapon_img_5, None, weapon_img_5)

    # ----------- Save file to the image ---------- #

    # Save this image
    background_img_0.save("images/result/png/profilePNG_"+current_number+".png", format="png")
    im = Image.open("images/result/png/profilePNG_"+current_number+".png")
    rgb_im = im.convert('RGB')
    rgb_im.save('images/result/jpg/profileJPG_'+current_number+'.jpg')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    loop_create_images([[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]])
    # loop_create_images()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
