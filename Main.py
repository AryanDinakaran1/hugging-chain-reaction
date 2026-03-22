from transformers import pipeline

model = pipeline("summarization", model="facebook/bart-large-cnn")
response = model("""Key Chapters of Don Toliver’s Story:
Early Life & Influences: Raised in the working-class Alief area of Houston, he grew up surrounded by music, listening to acts like Swishahouse, Stevie Wonder, and Marvin Gaye. His father was an aspiring musician, and early influences included hearing soul music in barber shops.
The Rise: Toliver started his career creating music with his friend Yungjosh93, releasing a mixtape called Playa Familia before launching his solo career.
The Cactus Jack Partnership: After a tumultuous beginning trying to make a name for himself, his manager, Cozy Kobe, helped connect him with Travis Scott's team. His career reached new heights after joining Cactus Jack Records, a joint venture with Atlantic Records.
"No Idea" & Stardom: In 2019, his song "No Idea" became a massive hit via TikTok, cementing his place in the mainstream music scene.
Sound Evolution: Known for a distinct melodic sound often referred to as "trap 'n' B," his musical style evolved from the R&B-infused Heaven or Hell (2020) and Life of a DON (2021) to the more soul-searching Love Sick (2023).
Latest Work & Persona: His 2024 album Hardstone Psycho marked a shift toward a "biker grunge" aesthetic, influenced by his personal passion for building and riding custom motorcycles.
Personal Life: In 2024, he and his partner, singer Kali Uchis, welcomed their first child.
Wikipedia
Wikipedia
 +8""")
print(response)

