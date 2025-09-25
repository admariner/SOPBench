cd ../..
devices="0"

model="claude-sonnet-4-20250514"
domains=("healthcare" "university" "dmv" "online_market" "bank" "hotel" "library")
tool_lists=("full")
method="fc"

for domain in "${domains[@]}"; do
    for tool_list in "${tool_lists[@]}"; do
        CUDA_VISIBLE_DEVICES=$devices python run_simulation.py \
                --domain $domain \
                --user_model adv \
                --assistant_model $model \
                --env_mode prompt \
                --tool_list $tool_list \
                --tool_call_mode $method \
                --num_run_per_interaction 1
    done
done